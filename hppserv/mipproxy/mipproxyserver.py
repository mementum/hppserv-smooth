#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of MipProxy
#
# MipProxy is a Microsoft Smooth Streaming Proxy Controller
# Copyright (C) 2011 Daniel Rodriguez
#
################################################################################
from collections import defaultdict

from hpproxy import HPProxyServer, ObjectHolder

from mipproxyhandler import MipProxyHandler


class MipProxyServer(HPProxyServer):
    PORT=HPProxyServer.PORT
    
    def __init__(self, host='localhost', port=PORT,
                 RequestHandlerClass=MipProxyHandler, controller=None, **kwargs):

        HPProxyServer.__init__(self, host, port, RequestHandlerClass, controller, **kwargs)

        if controller:
            self.mipcontrol = controller.mipcontrol
        else:
            self.mipcontrol = MipProxyServer.createconfig(self)

    @staticmethod
    def createconfig():
        mipcontrol = ObjectHolder()
        mipcontrol.started = True
        mipcontrol.bitrate = None
        mipcontrol.stats = defaultdict(float)
        mipcontrol.removerates = False
        mipcontrol.removeratesnum = 0
        mipcontrol.disablecaching = True
        return mipcontrol


def testMipProxyServer():
    mipproxyserver = MipProxyServer()
    mipproxyserver.setproxy(proxy=True, proxysystem=True, proxyurl='http://127.0.0.1:8888')
    mipproxyserver.serve_forever()


if __name__ == '__main__':
    testMipProxyServer()
