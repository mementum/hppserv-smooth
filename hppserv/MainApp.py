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
import wx

import MipFrame

def Run():
    mainApp = MainApp(0)
    mainApp.MainLoop()


class MainApp(wx.App):
    def OnInit(self):
        wx.Log_SetActiveTarget(wx.LogStderr())
        # wx.Log_SetActiveTarget(wx.LogBuffer())

        frame = MipFrame.MipFrame(None)
        self.SetTopWindow(frame)
        frame.Show(True)

        return True

