#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# This file is part of HPProxy (High Performance Proxy)
#
# HPProxy is a proxy engine designed to act mostly transparently to do
# modifications of requests and responses
#
# Copyright (C) 2011 Daniel Rodriguez
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/hpproxy
#
# HPProxy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HPProxy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HPProxy. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from BaseHTTPServer import BaseHTTPRequestHandler
from httplib import HTTPConnection
import rfc822
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
from urlparse import urlparse


class HPProxyHandler(BaseHTTPRequestHandler):
    # HTTPConnection.debuglevel = 2

    MessageClass = rfc822.Message
    server_version = "HPProxyServer"
    sys_version = '0.01'

    # To ensure that the connection remains open
    protocol_version = 'HTTP/1.1'

    def __init__(self, *args, **kwargs):
        self.parsed = urlparse('')
        self.conn = None
        self.numreq = 0
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)


    def log_message(self, format, *args):
        # To avoid unnecessary logging from the base class
        pass


    def finish(self):
        try:
            BaseHTTPRequestHandler.finish(self)            
        except:
            # Avoid cluttering from closed sockets exceptions
            # Since we only want to clean the request
            pass
        finally:
            try:
                self.wfile.close()
            except:
                pass
            try:
                self.rfile.close()
            except:
                pass


    def do_GET(self):
        # Request line: self.command, self.path, self.request_version
        # Headers: self.headers (rfc822.Message)
        # self.rfile, self.wfile - files opened on top of the request socket
        # self.close_connection too indicate that the connection shall be closed

        if self.server.doExit:
            self.close_connection = 1
            self.send_error(500, 'Server Closing Down')
            return

        self.numreq += 1 # Count the requests that this thread is handling

        # Remove the fp reference in the headers to avoid dangling reference
        self.headers.fp = None

        parsed = urlparse(self.path)

        config = self.server.config
        if config.proxy:
            if self.conn is None:
                connparsed = config.proxyparsed
        else:
            if parsed.netloc != self.parsed.netloc:
                if self.conn is not None:
                    # close the actual connection
                    self.conn.close()
                    self.conn = None
            # Point to destination
            self.parsed = parsed
            connparsed = self.parsed

        if self.conn is None:
            self.conn = HTTPConnection(host=connparsed.hostname,
                                       port=connparsed.port,
                                       timeout=config.timeout)

        # copy of request headers to keep original intact for later
        headers = self.headers.dict.copy()

        # Both are 1-hop, so we don't carry them over
        if 'connection' in headers:
            del headers['connection']
        # We may want to add our own
        if config.keepalive:
            headers['connection'] = 'keep-alive'
            
        if 'proxy-connection' in headers:
            del headers['proxy-connection']
        # we may also want to use the proxy-connection for upstream proxies
        if config.proxy and config.proxykeepalive:
            headers['proxy-connection'] = 'keep-alive'

        body = None
        if self.command.lower() == 'post':
            contenlength = headers.get('content-length', 0)
            body = self.rfile.read(contentlength)


        if hasattr(self, 'OnRequest'):
            command, path, body, headers = self.OnRequest(self.command, self.path, body, headers)
        else:
            command, path, body, headers = self.command, self.path, body, headers

        try:
            self.conn.request(method=command, url=path, body=body, headers=headers)
            # For POST ... I could write to the socket whatever "content-length" has ...
            # Although theoretically this could also be "chunked"
        except Exception, e:
            # self.logMsg('Exception happened during request: %s' % str(e), 2)
            self.send_error(400, str(e))
        else:
            try:
                hppresp = self.conn.getresponse()
            except Exception, e:
                # self.logMsg('Exception happened during getresponse: %s' % str(e), 2)
                self.send_error(400, str(e))
            else:
                if hasattr(self, 'OnResponseReceived'):
                    self.OnResponseReceived(command, path, body, headers, hppresp)
                # Prepare and send response
                self.send_response(hppresp.status, hppresp.reason)
                for header in hppresp.msg.keys():
                    values = hppresp.msg.getheaders(header)
                    for value in values:
                        valuelow = value.lower()
                        if header == 'transfer-encoding' and 'chunked' in valuelow:
                            # we will be dechunking
                            continue
                        # connection is 1-hop
                        if header in ['connection', 'proxy-connection']:
                            # 1 hop ... don't carry them over
                            continue
                        # Send the header: self.logMsg('Sending header %s:%s' % (key, header), 2)
                        self.send_header(header, value)

                # Reply with whatever it was requested, but adapted
                if 'connection' in self.headers:
                    self.send_header('connection', self.headers['connection'])
                if 'proxy-connection' in self.headers:
                    self.send_header('proxy-connection', self.headers['proxy-connection'])

                # add content-length if needed
                if hppresp.chunked:
                    # We are not sending the chunks so we need to add the "content-length header"
                    body = hppresp._read_chunked(None)
                    hppresp.close()
                    hppresp.chunked = False
                    hppresp.length = len(body)
                    hppresp.fp = StringIO(body)
                    self.send_header('content-length', '%d' % hppresp.length)

                # Finish headers
                self.end_headers()

                # Go with the body
                totaldata = 0
                if hppresp.chunked:
                    while not hppresp.isclosed():
                        data = hppresp.read(min(clength, 4096))
                        totaldata += len(data)
                        if data:
                            self.wfile.write(data)
                elif hppresp.length is not None:
                    clength = hppresp.length
                    while  clength > 0:
                        data = hppresp.read(min(clength, 4096))
                        totaldata += len(data)
                        clength -= len(data)
                        if data:
                            self.wfile.write(data)
                else:
                    pass

                if hppresp.will_close or self.close_connection:
                    self.conn.close()
                    self.conn = None

                # ensure the response is closed (and detached from the connection)
                hppresp.close()
                hppresp = None


    def postMsg(self, action, **kwargs):
        self.server.postMsg(action, **kwargs)


    def logMsg(self, logmsg, debuglevel=1):
        self.postMsg(action='log', logmsg=logmsg, debuglevel=debuglevel)
