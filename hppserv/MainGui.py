# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MipFrame
###########################################################################

class MipFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MIP Demo 1.00", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel10 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer121 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, u"Microsoft Experience Smooth Streaming URL" ), wx.HORIZONTAL )
		
		self.m_textCtrlSmoothUrl = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer7.Add( self.m_textCtrlSmoothUrl, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel10, wx.ID_ANY, u"Copy URL to Clipboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer18.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		self.m_button13 = wx.Button( self.m_panel10, wx.ID_ANY, u"About", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button13, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.LEFT, 5 )
		
		bSizer121.Add( bSizer18, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, u"Client" ), wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Requested Bitrate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		sbSizer4.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_gaugeBitrateRequested = wx.Gauge( self.m_panel10, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		sbSizer4.Add( self.m_gaugeBitrateRequested, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextBitrateRequested = wx.StaticText( self.m_panel10, wx.ID_ANY, u"....", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextBitrateRequested.Wrap( -1 )
		sbSizer4.Add( self.m_staticTextBitrateRequested, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer4.Add( sbSizer4, 0, wx.EXPAND|wx.RIGHT, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, u"Mip" ), wx.HORIZONTAL )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText40 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Allowed Bitrate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		bSizer24.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.m_gaugeBitrateAllowed = wx.Gauge( self.m_panel10, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_VERTICAL )
		bSizer24.Add( self.m_gaugeBitrateAllowed, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextBitrateAllowed = wx.StaticText( self.m_panel10, wx.ID_ANY, u"....", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextBitrateAllowed.Wrap( -1 )
		bSizer24.Add( self.m_staticTextBitrateAllowed, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		sbSizer5.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		self.m_sliderBitrateControl = wx.Slider( self.m_panel10, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH|wx.SL_INVERSE|wx.SL_LABELS|wx.SL_LEFT|wx.SL_VERTICAL )
		self.m_sliderBitrateControl.Enable( False )
		
		sbSizer5.Add( self.m_sliderBitrateControl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		bSizer4.Add( sbSizer5, 0, wx.EXPAND, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, u"Statistics" ), wx.HORIZONTAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText12 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Fragments Seen:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_staticTextNumFragments = wx.StaticText( self.m_panel10, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextNumFragments.Wrap( -1 )
		fgSizer2.Add( self.m_staticTextNumFragments, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText121 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Average Bitrate downloaded:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )
		self.m_staticText121.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText121, 0, wx.ALL, 5 )
		
		self.m_staticTextAvgBitratePlayed = wx.StaticText( self.m_panel10, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAvgBitratePlayed.Wrap( -1 )
		fgSizer2.Add( self.m_staticTextAvgBitratePlayed, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText1211 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Video data downloaded:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1211.Wrap( -1 )
		self.m_staticText1211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText1211, 0, wx.ALL, 5 )
		
		self.m_staticTextVideoDataDown = wx.StaticText( self.m_panel10, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextVideoDataDown.Wrap( -1 )
		fgSizer2.Add( self.m_staticTextVideoDataDown, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText1212 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Average Bitrate requested:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1212.Wrap( -1 )
		self.m_staticText1212.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText1212, 0, wx.ALL, 5 )
		
		self.m_staticTextAvgBitrateRequested = wx.StaticText( self.m_panel10, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAvgBitrateRequested.Wrap( -1 )
		fgSizer2.Add( self.m_staticTextAvgBitrateRequested, 0, wx.ALL, 5 )
		
		self.m_staticText12111 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Video data requested:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12111.Wrap( -1 )
		self.m_staticText12111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText12111, 0, wx.ALL, 5 )
		
		self.m_staticTextVideoDataReq = wx.StaticText( self.m_panel10, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextVideoDataReq.Wrap( -1 )
		fgSizer2.Add( self.m_staticTextVideoDataReq, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText121111 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Video data saved:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121111.Wrap( -1 )
		self.m_staticText121111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText121111, 0, wx.ALL, 5 )
		
		self.m_staticTextVideoDataSaved = wx.StaticText( self.m_panel10, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextVideoDataSaved.Wrap( -1 )
		fgSizer2.Add( self.m_staticTextVideoDataSaved, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer11.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer4.Add( sbSizer11, 1, wx.EXPAND|wx.LEFT, 5 )
		
		bSizer121.Add( bSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer121.Add( self.m_staticline2, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, u"Video Bitrates" ), wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, u"Available at Server" ), wx.VERTICAL )
		
		m_listBoxVideoBitratesServerChoices = []
		self.m_listBoxVideoBitratesServer = wx.ListBox( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxVideoBitratesServerChoices, 0 )
		sbSizer8.Add( self.m_listBoxVideoBitratesServer, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer14.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		sbSizer81 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, u"Seen by client" ), wx.VERTICAL )
		
		m_listBoxVideoBitratesClientChoices = []
		self.m_listBoxVideoBitratesClient = wx.ListBox( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxVideoBitratesClientChoices, 0 )
		sbSizer81.Add( self.m_listBoxVideoBitratesClient, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer14.Add( sbSizer81, 1, wx.EXPAND|wx.LEFT, 5 )
		
		sbSizer3.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		self.m_staticline6 = wx.StaticLine( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer3.Add( self.m_staticline6, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxRemoveBitrates = wx.CheckBox( self.m_panel10, wx.ID_ANY, u"Don't send highest", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_checkBoxRemoveBitrates, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_spinCtrlRemoveBitrates = wx.SpinCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer15.Add( self.m_spinCtrlRemoveBitrates, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_staticText9 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"bitrates to client", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer15.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer3.Add( bSizer15, 0, wx.EXPAND, 5 )
		
		bSizer21.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, u"Proy Network Details" ), wx.VERTICAL )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBoxOnlyLocalConnections = wx.CheckBox( self.m_panel10, wx.ID_ANY, u"Listen only for local connections", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.m_checkBoxOnlyLocalConnections, 0, wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Listen on Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer9.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_textCtrlMipPort = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer9.Add( self.m_textCtrlMipPort, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		bSizer141.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		sbSizer2.Add( bSizer141, 0, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer2.Add( self.m_staticline3, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_checkBoxUseSystemDefaultProxy = wx.CheckBox( self.m_panel10, wx.ID_ANY, u"Use System Proxy as Upstream", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_checkBoxUseSystemDefaultProxy, 0, wx.ALL, 5 )
		
		self.m_staticline31 = wx.StaticLine( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer2.Add( self.m_staticline31, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_checkBoxUseUpStreamProxy = wx.CheckBox( self.m_panel10, wx.ID_ANY, u"Use Other Upstream Proxy", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_checkBoxUseUpStreamProxy, 0, wx.ALL, 5 )
		
		self.m_textCtrlProxyUrl = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_textCtrlProxyUrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_panel3 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.Enable( False )
		self.m_panel3.Hide()
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"Proxy Authentication" ), wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText16 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer1.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_textCtrlProxyUsername = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrlProxyUsername, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText17 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer1.Add( self.m_staticText17, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_textCtrlProxyPassword = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer1.Add( self.m_textCtrlProxyPassword, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		sbSizer15.Add( fgSizer1, 0, wx.EXPAND|wx.LEFT, 5 )
		
		self.m_panel3.SetSizer( sbSizer15 )
		self.m_panel3.Layout()
		sbSizer15.Fit( self.m_panel3 )
		sbSizer2.Add( self.m_panel3, 1, wx.EXPAND, 5 )
		
		bSizer21.Add( sbSizer2, 0, wx.EXPAND|wx.LEFT, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, u"MIP Control" ), wx.VERTICAL )
		
		
		sbSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_buttonMipStart = wx.Button( self.m_panel10, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_buttonMipStart, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_buttonMipPause = wx.Button( self.m_panel10, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonMipPause.Enable( False )
		
		sbSizer1.Add( self.m_buttonMipPause, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_buttonMipStop = wx.Button( self.m_panel10, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonMipStop.Enable( False )
		
		sbSizer1.Add( self.m_buttonMipStop, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline19 = wx.StaticLine( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer1.Add( self.m_staticline19, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_checkBoxBrowserCaching = wx.CheckBox( self.m_panel10, wx.ID_ANY, u"Disable Caching", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_checkBoxBrowserCaching, 0, wx.ALL, 5 )
		
		
		sbSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer21.Add( sbSizer1, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		bSizer121.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		self.m_staticline21 = wx.StaticLine( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer121.Add( self.m_staticline21, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, u"Log" ), wx.VERTICAL )
		
		self.m_textCtrlMipLog = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer6.Add( self.m_textCtrlMipLog, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonCopyLogToClipboard = wx.Button( self.m_panel10, wx.ID_ANY, u"Copy Log to Clipboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_buttonCopyLogToClipboard, 0, wx.ALL, 5 )
		
		self.m_buttonClearLog = wx.Button( self.m_panel10, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_buttonClearLog, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		sbSizer6.Add( bSizer12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer121.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		bSizer20.Add( bSizer121, 1, wx.EXPAND, 5 )
		
		self.m_panel10.SetSizer( bSizer20 )
		self.m_panel10.Layout()
		bSizer20.Fit( self.m_panel10 )
		bSizer3.Add( self.m_panel10, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_panel5.SetSizer( bSizer3 )
		self.m_panel5.Layout()
		bSizer3.Fit( self.m_panel5 )
		bSizer2.Add( self.m_panel5, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer2 )
		self.Layout()
		bSizer2.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnButtonClickCopyUrlToClipboard )
		self.m_button13.Bind( wx.EVT_BUTTON, self.OnButtonClickAbout )
		self.m_sliderBitrateControl.Bind( wx.EVT_SCROLL_CHANGED, self.OnScrollChangedBitrateControl )
		self.m_checkBoxRemoveBitrates.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxRemoveRates )
		self.m_spinCtrlRemoveBitrates.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrlRemoveRates )
		self.m_checkBoxUseSystemDefaultProxy.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxUseSystemDefaultProxy )
		self.m_checkBoxUseUpStreamProxy.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxUserUpstreamProxy )
		self.m_buttonMipStart.Bind( wx.EVT_BUTTON, self.OnButtonClickMipStart )
		self.m_buttonMipPause.Bind( wx.EVT_BUTTON, self.OnButtonClickMipPause )
		self.m_buttonMipStop.Bind( wx.EVT_BUTTON, self.OnButtonClickMipStop )
		self.m_checkBoxBrowserCaching.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxDisableBrowserCaching )
		self.m_buttonCopyLogToClipboard.Bind( wx.EVT_BUTTON, self.OnButtonClickCopyLogToClipboard )
		self.m_buttonClearLog.Bind( wx.EVT_BUTTON, self.OnButtonClickClearLog )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonClickCopyUrlToClipboard( self, event ):
		event.Skip()
	
	def OnButtonClickAbout( self, event ):
		event.Skip()
	
	def OnScrollChangedBitrateControl( self, event ):
		event.Skip()
	
	def OnCheckBoxRemoveRates( self, event ):
		event.Skip()
	
	def OnSpinCtrlRemoveRates( self, event ):
		event.Skip()
	
	def OnCheckBoxUseSystemDefaultProxy( self, event ):
		event.Skip()
	
	def OnCheckBoxUserUpstreamProxy( self, event ):
		event.Skip()
	
	def OnButtonClickMipStart( self, event ):
		event.Skip()
	
	def OnButtonClickMipPause( self, event ):
		event.Skip()
	
	def OnButtonClickMipStop( self, event ):
		event.Skip()
	
	def OnCheckBoxDisableBrowserCaching( self, event ):
		event.Skip()
	
	def OnButtonClickCopyLogToClipboard( self, event ):
		event.Skip()
	
	def OnButtonClickClearLog( self, event ):
		event.Skip()
	

