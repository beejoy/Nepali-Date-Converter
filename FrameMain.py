#Boa:Frame:FrameMain

import wx
import string
import dateconverter

def create(parent):
    return FrameMain(parent)

[wxID_FRAMEMAIN, wxID_FRAMEMAINBTNAD2BS, wxID_FRAMEMAINBTNBS2AD, 
 wxID_FRAMEMAINPANEL1, wxID_FRAMEMAINSTCONVERTEDDATE, 
 wxID_FRAMEMAINSTSOURCEDATE, wxID_FRAMEMAINTXTCONVERTEDDATE, 
 wxID_FRAMEMAINTXTSOURCEDATE, 
] = [wx.NewId() for _init_ctrls in range(8)]

class FrameMain(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEMAIN, name=u'FrameMain',
              parent=prnt, pos=wx.Point(425, 381), size=wx.Size(420, 144),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Date Converter')
        self.SetClientSize(wx.Size(420, 144))
        self.Center(wx.BOTH)

        self.panel1 = wx.Panel(id=wxID_FRAMEMAINPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(420, 144),
              style=wx.TAB_TRAVERSAL)

        self.stSourceDate = wx.StaticText(id=wxID_FRAMEMAINSTSOURCEDATE,
              label=u'Source Date:', name=u'stSourceDate', parent=self.panel1,
              pos=wx.Point(24, 21), size=wx.Size(83, 16), style=0)

        self.stConvertedDate = wx.StaticText(id=wxID_FRAMEMAINSTCONVERTEDDATE,
              label=u'Converted Date:', name=u'stConvertedDate',
              parent=self.panel1, pos=wx.Point(24, 62), size=wx.Size(106, 16),
              style=0)

        self.txtSourceDate = wx.TextCtrl(id=wxID_FRAMEMAINTXTSOURCEDATE,
              name=u'txtSourceDate', parent=self.panel1, pos=wx.Point(152, 16),
              size=wx.Size(232, 27), style=0, value=u'2068-5-27')
        self.txtSourceDate.SetToolTipString(u'Enter source date in YYYY-MM-DD format.')

        self.txtConvertedDate = wx.TextCtrl(id=wxID_FRAMEMAINTXTCONVERTEDDATE,
              name=u'txtConvertedDate', parent=self.panel1, pos=wx.Point(152,
              56), size=wx.Size(232, 27), style=0, value=u'')
        self.txtConvertedDate.SetEditable(False)

        self.btnBS2AD = wx.Button(id=wxID_FRAMEMAINBTNBS2AD, label=u'BS to AD',
              name=u'btnBS2AD', parent=self.panel1, pos=wx.Point(152, 97),
              size=wx.Size(112, 29), style=0)
        self.btnBS2AD.Bind(wx.EVT_BUTTON, self.OnBtnBS2ADButton,
              id=wxID_FRAMEMAINBTNBS2AD)

        self.btnAD2BS = wx.Button(id=wxID_FRAMEMAINBTNAD2BS, label=u'AD to BS',
              name=u'btnAD2BS', parent=self.panel1, pos=wx.Point(272, 97),
              size=wx.Size(112, 29), style=0)
        self.btnAD2BS.Bind(wx.EVT_BUTTON, self.OnBtnAD2BSButton,
              id=wxID_FRAMEMAINBTNAD2BS)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def TupleFromString(self, strval, separator):
        lst = string.split(strval, separator)
        return tuple([int(lst[0]), int(lst[1]), int(lst[2])])
    
    def OnBtnBS2ADButton(self, event):
        #lst = string.split(self.txtSourceDate.GetValue(), '-')
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
