# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.animate

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
		
		self.m_animCtrl2 = wx.animate.AnimationCtrl( self, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE ) 
		
		self.m_animCtrl2.SetInactiveBitmap( wx.Bitmap( u"gato.gif", wx.BITMAP_TYPE_ANY ) )
		self.m_mgr.AddPane( self.m_animCtrl2, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
		
		
		self.m_mgr.Update()
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	

