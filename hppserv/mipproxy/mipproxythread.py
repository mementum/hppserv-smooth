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

from mipproxyserver import MipProxyServer
from hpproxy import HPProxyThread


class MipProxyThread(HPProxyThread):
    PORT = HPProxyThread.PORT
    
    def __init__(self, host='localhost', port=PORT, **kwargs):
        HPProxyThread.__init__(self, host, port, proxyclass=MipProxyServer, **kwargs)
        self.mipcontrol = MipProxyServer.createconfig()


    def bitrate(self, bitrate):
        self.mipcontrol.bitrate = bitrate


    def pause(self):
        self.mipcontrol.started = False


    def unpause(self):
        self.mipcontrol.started = True


    def removerates(self, removerates, removeratesnum):
        self.mipcontrol.removerates = removerates
        self.mipcontrol.removeratesnum = removeratesnum


    def disablecaching(self, onoff):
        self.mipcontrol.disablecaching = onoff
