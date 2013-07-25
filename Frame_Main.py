# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Frame_Main
###########################################################################

class Frame_Main ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 853,595 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"信号采集" ), wx.HORIZONTAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"开始采集", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"采集完毕", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"拼读", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_button10, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"保存样本", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( sbSizer1, 0, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"数据分析" ), wx.HORIZONTAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"预加重", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"加窗分帧", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button5, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"短时能量", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button6, 0, wx.ALL, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"过零率", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button11, 0, wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, u"端点检测", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_button8 = wx.Button( self, wx.ID_ANY, u"获取特征", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button8, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self, wx.ID_ANY, u"显示全部", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer2, 0, 0, 5 )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel1, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		sbSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.Sound_Make )
		self.m_button2.Bind( wx.EVT_BUTTON, self.Sound_Stop )
		self.m_button10.Bind( wx.EVT_BUTTON, self.Sound_Say )
		self.m_button3.Bind( wx.EVT_BUTTON, self.Sound_Save )
		self.m_button4.Bind( wx.EVT_BUTTON, self.Signal_Height )
		self.m_button5.Bind( wx.EVT_BUTTON, self.Singan_Frame )
		self.m_button6.Bind( wx.EVT_BUTTON, self.Signal_En )
		self.m_button11.Bind( wx.EVT_BUTTON, self.Signal_Zero )
		self.m_button7.Bind( wx.EVT_BUTTON, self.Signal_Point )
		self.m_button8.Bind( wx.EVT_BUTTON, self.Signal_MEFF )
		self.m_button9.Bind( wx.EVT_BUTTON, self.Signal_Show )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Sound_Make( self, event ):
		event.Skip()
	
	def Sound_Stop( self, event ):
		event.Skip()
	
	def Sound_Say( self, event ):
		event.Skip()
	
	def Sound_Save( self, event ):
		event.Skip()
	
	def Signal_Height( self, event ):
		event.Skip()
	
	def Singan_Frame( self, event ):
		event.Skip()
	
	def Signal_En( self, event ):
		event.Skip()
	
	def Signal_Zero( self, event ):
		event.Skip()
	
	def Signal_Point( self, event ):
		event.Skip()
	
	def Signal_MEFF( self, event ):
		event.Skip()
	
	def Signal_Show( self, event ):
		event.Skip()
	

