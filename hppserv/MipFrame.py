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
from datetime import datetime

import wx

import MainGui

from mipproxy import MipProxyThread as MipProxy

# Implementing MipFrame
class MipFrame(MainGui.MipFrame):
    def __init__(self, parent):
	MainGui.MipFrame.__init__(self, parent)
        self.m_textCtrlSmoothUrl.SetValue('http://www.iis.net/media/experiencesmoothstreaming')
	self.mipproxy = MipProxy(frame=self, function=self.OnMipProxy)

        # Standard for a local intermediate proxy
        self.m_textCtrlProxyUrl.SetValue('http://127.0.0.1:8888')

        # Sensible defaults for the local connections and port
        self.m_textCtrlMipPort.SetValue(str(MipProxy.PORT))
        self.m_checkBoxOnlyLocalConnections.SetValue(True)

        # These values may be read from the configuration of the mipproxyserver
        self.m_checkBoxBrowserCaching.SetValue(True)


    def OnButtonClickAbout(self, event):
        wx.MessageBox('Copyright (C) 2011 Daniel Rodriguez', 'About')

	
    # Handlers for MipFrame events.
    def OnButtonClickMipStart(self, event):
        self.m_buttonMipStart.Disable()
        self.m_buttonMipPause.Enable()
        self.m_buttonMipStop.Enable()

        self.m_checkBoxOnlyLocalConnections.Disable()
        self.m_textCtrlMipPort.Disable()

        startdetails = dict()
        # Browser is doing the authentication
        # startdetails['username'] = self.m_textCtrlProxyUsername.GetValue()
        # startdetails['password'] = self.m_textCtrlProxyPassword.GetValue()

        # Listening details
        startdetails['port'] = int(self.m_textCtrlMipPort.GetValue())
        startdetails['host'] = 'localhost' if self.m_checkBoxOnlyLocalConnections.GetValue() else ''

        # Proxy details
        upstreamproxy = self.m_checkBoxUseUpStreamProxy.GetValue()
        upstreamproxysystem = self.m_checkBoxUseSystemDefaultProxy.GetValue()
        startdetails['proxy'] = upstreamproxy or upstreamproxysystem
        startdetails['proxyurl'] = self.m_textCtrlProxyUrl.GetValue()
        startdetails['proxysystem'] = upstreamproxysystem
        self.mipproxy.proxystart(**startdetails)

        if hasattr(self, 'videoBitrates') and self.videoBitrates:
            self.m_sliderBitrateControl.Enable()
        self.m_checkBoxRemoveBitrates.Enable()
        self.m_spinCtrlRemoveBitrates.Enable()


    def OnButtonClickMipStop(self, event):
        self.mipproxy.proxystop()
        self.m_buttonMipStart.Enable()
        self.m_buttonMipPause.Disable()
        self.m_buttonMipPause.SetLabel('Pause')
        self.m_buttonMipStop.Disable()
        self.m_checkBoxOnlyLocalConnections.Enable()
        self.m_textCtrlMipPort.Enable()
        self.m_sliderBitrateControl.Disable()


    def OnButtonClickMipPause(self, event):
        label = self.m_buttonMipPause.GetLabel()
        if label == 'Pause':
            self.mipproxy.pause()
            self.m_buttonMipPause.SetLabel('UnPause')
        else:
            self.mipproxy.unpause()
            self.m_buttonMipPause.SetLabel('Pause')

	
    def OnCheckBoxUserUpstreamProxy(self, event):
        pass
	
    def OnCheckBoxUseSystemDefaultProxy(self, event):
	# TODO: Implement OnCheckBoxUserUpstreamProxy

        onOff = self.m_checkBoxUseSystemDefaultProxy.GetValue()

        self.m_checkBoxUseUpStreamProxy.Enable(not onOff)


    def OnButtonClickClearLog(self, event):
        self.m_textCtrlMipLog.ChangeValue('')


    def OnButtonClickCopyUrlToClipboard(self, event):
        copytxt = self.m_textCtrlSmoothUrl.GetValue()
        if copytxt and wx.TheClipboard.Open():
            wx.TheClipboard.AddData(wx.TextDataObject(copytxt))
            wx.TheClipboard.Close()

        
    def OnCheckBoxRemoveRates(self, event):
        removerates = self.m_checkBoxRemoveBitrates.GetValue()
        removeratesnum = self.m_spinCtrlRemoveBitrates.GetValue()
        self.mipproxy.removerates(removerates, removeratesnum)


    def OnSpinCtrlRemoveRates(self, event):
        removerates = self.m_checkBoxRemoveBitrates.GetValue()
        removeratesnum = self.m_spinCtrlRemoveBitrates.GetValue()
        self.mipproxy.removerates(removerates, removeratesnum)


    def OnButtonClickCopyLogToClipboard(self, event):
        copytxt = self.m_textCtrlMipLog.GetValue()
        if copytxt and wx.TheClipboard.Open():
            wx.TheClipboard.AddData(wx.TextDataObject(copytxt))
            wx.TheClipboard.Close()

        
    def OnScrollChangedBitrateControl(self, event):
        pos = self.m_sliderBitrateControl.GetValue()

        vbrate = self.videoBitrates[pos]
        # Change the "allowed" gauge
        self.m_gaugeBitrateAllowed.SetValue(pos)
        self.m_staticTextBitrateAllowed.SetLabel('%.2f Kbps' % (vbrate / 1000.0))
        # tell the controller
        self.mipproxy.bitrate(vbrate)


    def OnCheckBoxDisableBrowserCaching	(self, event):
        self.mipproxy.disablecaching(self.m_checkBoxBrowserCaching.GetValue())

        
    def OnMipProxy(self, event):
        msg = event.msg
        if msg.action == 'log':
            # Log Message
            self.m_textCtrlMipLog.AppendText('%s: %s\r\n' % (datetime.now().isoformat(), msg.logmsg))
            
        elif msg.action == 'videoBitrates':
            # Manifest - VideoBitrates
            self.videoBitratesServer = msg.videoBitratesServer
            self.videoBitratesClient = msg.videoBitratesClient
            self.videoBitratesServer.sort(reverse=False)
            self.videoBitratesClient.sort(reverse=False)

            self.videoBitrates = self.videoBitratesClient

            self.m_listBoxVideoBitratesServer.Clear()
            for vbrate in self.videoBitratesServer:
                self.m_listBoxVideoBitratesServer.Append(str(vbrate))
                self.m_listBoxVideoBitratesServer.Refresh()

            self.m_listBoxVideoBitratesClient.Clear()
            for vbrate in self.videoBitratesClient:
                self.m_listBoxVideoBitratesClient.Append(str(vbrate))
                self.m_listBoxVideoBitratesClient.Refresh()

            numrates = len(self.videoBitrates) - 1
            self.m_gaugeBitrateRequested.SetRange(numrates)
            self.m_gaugeBitrateAllowed.SetRange(numrates)
            self.m_gaugeBitrateAllowed.SetValue(numrates)
            self.m_staticTextBitrateAllowed.SetLabel('%.2f Kbps' % (self.videoBitrates[numrates] / 1000.0))
            self.m_sliderBitrateControl.SetRange(0, numrates)
            self.m_sliderBitrateControl.SetValue(numrates)

            if numrates:
                self.m_sliderBitrateControl.Enable()

        elif msg.action == 'requestedRate':
            # Manifest - VideoBitrates
            pos = self.videoBitrates.index(msg.bitrate)
            self.m_gaugeBitrateRequested.SetValue(pos)
            self.m_staticTextBitrateRequested.SetLabel('%.2f Kbps' % (msg.bitrate / 1000.0))

        elif msg.action == 'statistics':
            # Manifest - VideoBitrates
            self.m_staticTextNumFragments.SetLabel(str(int(msg.seenfragments)))

            value = '%d Kbps' % (msg.avgbitratedown/1000.0)
            self.m_staticTextAvgBitratePlayed.SetLabel(value)

            value = '%.2f Mbytes' % (msg.videodatadown/8.0/1024.0/1024.0)
            self.m_staticTextVideoDataDown.SetLabel(value)

            value = '%d Kbps' % (msg.avgbitratereq/1000.0)
            self.m_staticTextAvgBitrateRequested.SetLabel(value)

            value = '%.2f Mbytes' % (msg.videodatareq/8.0/1024.0/1024.0)
            self.m_staticTextVideoDataReq.SetLabel(value)

            value = '%.2f Mbytes' % (msg.videodatasaved/8.0/1024.0/1024.0)
            self.m_staticTextVideoDataSaved.SetLabel(value)
        else:
            # Unknown message
            pass

        pass
