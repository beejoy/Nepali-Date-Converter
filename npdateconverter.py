#!/usr/bin/env python
#Boa:Frame:FrameMain

import wx
import string
import dateconverter
from wx.lib.anchors import LayoutAnchors

def create(parent):
    return FrameMain(parent)

[wxID_FRAMEMAIN, wxID_FRAMEMAINBTNAD2BS, wxID_FRAMEMAINBTNBS2AD, 
 wxID_FRAMEMAINPANEL1, wxID_FRAMEMAINSTCONVERTEDDATE, wxID_FRAMEMAINSTEXAMPLE, 
 wxID_FRAMEMAINSTSOURCEDATE, wxID_FRAMEMAINTXTCONVERTEDDATE, 
 wxID_FRAMEMAINTXTSOURCEDATE, 
] = [wx.NewId() for _init_ctrls in range(9)]

class FrameMain(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEMAIN, name=u'FrameMain',
              parent=prnt, pos=wx.Point(462, 368), size=wx.Size(395, 168),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Date Converter')
        self.SetClientSize(wx.Size(395, 168))
        self.Center(wx.BOTH)

        self.panel1 = wx.Panel(id=wxID_FRAMEMAINPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(395, 168),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetConstraints(LayoutAnchors(self.panel1, True, True, False,
              False))

        self.stSourceDate = wx.StaticText(id=wxID_FRAMEMAINSTSOURCEDATE,
              label=u'Source Date:', name=u'stSourceDate', parent=self.panel1,
              pos=wx.Point(23, 22), size=wx.Size(83, 17), style=0)

        self.stConvertedDate = wx.StaticText(id=wxID_FRAMEMAINSTCONVERTEDDATE,
              label=u'Converted Date:', name=u'stConvertedDate',
              parent=self.panel1, pos=wx.Point(23, 77), size=wx.Size(106, 17),
              style=0)

        self.txtSourceDate = wx.TextCtrl(id=wxID_FRAMEMAINTXTSOURCEDATE,
              name=u'txtSourceDate', parent=self.panel1, pos=wx.Point(136, 16),
              size=wx.Size(232, 27), style=0, value=u'')

        self.txtConvertedDate = wx.TextCtrl(id=wxID_FRAMEMAINTXTCONVERTEDDATE,
              name=u'txtConvertedDate', parent=self.panel1, pos=wx.Point(136,
              72), size=wx.Size(232, 27), style=0, value=u'')

        self.stExample = wx.StaticText(id=wxID_FRAMEMAINSTEXAMPLE,
              label=u'(e.g. 2008-9-9)', name=u'stExample', parent=self.panel1,
              pos=wx.Point(142, 50), size=wx.Size(81, 13), style=0)
        self.stExample.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False,
              u'Sans'))
        self.stExample.SetForegroundColour(wx.Colour(219, 58, 55))

        self.btnBS2AD = wx.Button(id=wxID_FRAMEMAINBTNBS2AD, label=u'BS to AD',
              name=u'btnBS2AD', parent=self.panel1, pos=wx.Point(136, 119),
              size=wx.Size(104, 29), style=0)
        self.btnBS2AD.Bind(wx.EVT_BUTTON, self.OnBtnBS2ADButton,
              id=wxID_FRAMEMAINBTNBS2AD)

        self.btnAD2BS = wx.Button(id=wxID_FRAMEMAINBTNAD2BS, label=u'AD to BS',
              name=u'btnAD2BS', parent=self.panel1, pos=wx.Point(248, 120),
              size=wx.Size(104, 29), style=0)
        self.btnAD2BS.Bind(wx.EVT_BUTTON, self.OnBtnAD2BSButton,
              id=wxID_FRAMEMAINBTNAD2BS)
        
        favicon = wx.Icon('favicon.ico', wx.BITMAP_TYPE_ICO, 16, 16)
        wx.Frame.SetIcon(self, favicon)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def TupleFromString(self, strval, separator):
        lst = string.split(strval, separator)
        return tuple([int(lst[0]), int(lst[1]), int(lst[2])])
    
    def OnBtnBS2ADButton(self, event):
        tplSrc = self.TupleFromString(self.txtSourceDate.GetValue(), '-')
        
        converter = dateconverter.NepaliDateConverter()
        try:
            src_date = converter.bs2ad(tplSrc)
            self.txtConvertedDate.SetValue(converter.format_date(src_date, 'ad'))
        except:
            self.txtConvertedDate.Value = "Invalid date value encountered!"

    def OnBtnAD2BSButton(self, event):
        tplSrc = self.TupleFromString(self.txtSourceDate.GetValue(), '-')
        
        converter = dateconverter.NepaliDateConverter()
        try:
            src_date = converter.ad2bs(tplSrc)
            self.txtConvertedDate.SetValue(converter.format_date(src_date, 'np'))
        except:
            self.txtConvertedDate.Value = "Invalid date value encountered!"

if __name__ == "__main__":
    app = wx.App()
    frame = create(None)
    frame.Show()
    app.MainLoop()
