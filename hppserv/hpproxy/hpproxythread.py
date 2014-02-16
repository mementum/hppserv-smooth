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
from Queue import Queue
from threading import Thread

from hpproxy import HPProxyServer
from hpputil import ObjectHolder

import wx

class HPPEvent(wx.PyEvent):
    def __init__(self, pyEventId, msg=None):
        wx.PyEvent.__init__(self)
        self.SetEventType(pyEventId)
        self.msg = msg


class HPProxyThread(Thread):
    PORT = HPProxyServer.PORT

    def __init__(self, host='localhost', port=PORT, proxyclass=HPProxyServer, **kwargs):
        Thread.__init__(self)
        self.qmsg = Queue()
        self.host = host
        self.port = port
        self.proxyclass = proxyclass

        self.frame = kwargs.get('frame', None)
        self.function = kwargs.get('function', None)
        self.pyEventId = wx.NewId()
        if self.frame and self.function:
            self.frame.Connect(wx.ID_ANY, wx.ID_ANY, self.pyEventId, self.function)

        self.daemon = True
        self.start()


    def run(self):
        while True:
            msg = self.qmsg.get(block=True)
            self.proxyserver = self.proxyclass(msg.host, msg.port, controller=self)
            self.proxyserver.doExit = False
            self.setproxyupstream(msg.proxy, msg.proxysystem, msg.proxyurl)
            self.proxyserver.serve_forever()


    def postMsg(self, action, **kwargs):
        if self.frame:
            msg = ObjectHolder(action=action, **kwargs)
            wx.PostEvent(self.frame, HPPEvent(self.pyEventId, msg))


    def setproxy(self, proxy, proxysystem=False, proxyurl=None):
        self.setproxyupstream(proxy, proxysystem, proxyurl)


    def setproxyupstream(self, proxy, proxysystem=False, proxyurl=None):
        self.proxyserver.setproxyupstream(proxy, proxysystem, proxyurl)


    def proxystart(self, **kwargs):
        if 'port' not in kwargs:
            kwargs['port'] = self.port
        if 'host' not in kwargs:
            kwargs['host'] = self.host
        self.qmsg.put(ObjectHolder(**kwargs))


    def proxystop(self):
        self.proxyserver.doExit = True
        self.proxyserver.shutdown()
        try:
            self.proxyserver.socket.close() # to free the port
        except:
            pass
        finally:
            self.proxyserver = None

