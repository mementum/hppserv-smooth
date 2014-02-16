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
from BaseHTTPServer import HTTPServer
from datetime import datetime
from SocketServer import ThreadingMixIn
import urllib
from urlparse import urlparse

from hpproxyhandler import HPProxyHandler
from hpputil import ObjectHolder


class HPProxyServer(ThreadingMixIn, HTTPServer):
    DEBUGLEVEL = 1
    PORT = 9000

    def __init__(self, host='localhost', port=PORT,
                 RequestHandlerClass=HPProxyHandler, controller=None,
                 **kwargs):

        HTTPServer.__init__(self, (host, port), RequestHandlerClass)

        # External controller from thread
        self.controller = controller

        # Control variables
        self.config = ObjectHolder()
        self.config.proxy = False
        self.config.proxyurl = ''
        self.config.proxyparsed = urlparse(self.config.proxyurl)

        self.config.keepalive = kwargs.get('keepalive', False)
        self.config.proxykeepalive = kwargs.get('proxykeepalive', False)
        self.config.timeout = kwargs.get('timeout', 10)
        self.config.debuglevel = kwargs.get('debuglevel', HPProxyServer.DEBUGLEVEL)

    def setproxy(self, proxy, proxysystem=False, proxyurl=None):
        self.setproxyupstream(proxy, proxysystem, proxyurl)


    def setproxyupstream(self, proxy, proxysystem=False, proxyurl=None):
        if proxysystem:
            proxyurl = None
            proxies = urllib.getproxies()
            for scheme, url in proxies.iteritems():
                if scheme.lower() == 'http':
                    proxyurl = proxies[scheme]
                    break

        if proxyurl:
            self.config.proxyurl = proxyurl
            self.config.proxyparsed = urlparse(self.config.proxyurl)

        self.config.proxy = proxy


    def postMsg(self, action, **kwargs):
        if self.controller is not None:
            self.controller.postMsg(action, **kwargs)
        elif action == 'log':
            # Don't let messages go away
            if kwargs.get('debuglevel', 1) <= self.config.debuglevel:
                print '%s: %s' % (datetime.now().isoformat(), kwargs.get('logmsg', ''))

            
def testHPProxyServer():
    hpproxyserver  = HPProxyServer()
    # hpproxyserver.setproxy(proxy=True, proxysystem=False, proxyurl='http://127.0.0.1:8888')
    hpproxyserver.serve_forever()


if __name__ == '__main__':
    testHPProxyServer()
