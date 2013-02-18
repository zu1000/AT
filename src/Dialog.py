import wx, sys

OK_ID = wx.NewId()
CLOSE_ID = wx.NewId()

class CtrSelectorPanel(wx.Panel):
    def __init__(self, *args, **kw):
        wx.Panel.__init__(self, *args, **kw)

        self.InitPanel()

        self.selected = list()

    def InitPanel(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.lst = wx.ListCtrl(self, -1, style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        self.PopulateList()
        vbox.Add(self.lst, 1, wx.EXPAND)
        self.SetSizer(vbox)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSeleted, self.lst)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected, self.lst)

    def PopulateList(self):
        self.lst.InsertColumn(0, "Name")
        self.lst.InsertColumn(0, "Type")
        
        for i in range(50):
            index = self.lst.InsertStringItem(sys.maxint, "GOLD" + str(i))
            self.lst.SetStringItem(index, 1, "Future")

        index = self.lst.InsertStringItem(sys.maxint, "OIL")
        self.lst.SetStringItem(index, 1, "Future")

    def OnItemSeleted(self, evt):
        print evt.m_itemIndex
        print "Select " + self.lst.GetItem(evt.m_itemIndex, 0).GetText()
        selected = self.lst.GetItem(evt.m_itemIndex, 0).GetText()
        if (selected not in self.selected):
            self.selected.append(selected)
        pass

    def OnItemDeselected(self, evt):
        print evt.m_itemIndex
        print "Deselect " + self.lst.GetItem(evt.m_itemIndex, 0).GetText()
        deselected = self.lst.GetItem(evt.m_itemIndex, 0).GetText()
        if (deselected in self.selected):
            self.selected.remove(deselected)
        pass


class CtrSelector(wx.Dialog):
    def __init__(self, *args, **kw):
        wx.Dialog.__init__(self, *args, **kw)

        self.InitLayout()
        self.SetTitle("Contract Selector")

    def InitLayout(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.pnl = CtrSelectorPanel(self)
        vbox.Add(self.pnl, 1, wx.ALL|wx.EXPAND)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label="Ok", id=OK_ID)
        clButton = wx.Button(self, label="Close", id=CLOSE_ID)
        hbox.Add(okButton)
        hbox.Add(clButton, flag=wx.LEFT, border=5)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)
        self.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.OnOk, id=OK_ID)
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=CLOSE_ID)

    def GetSelected(self):
        if (self.pnl is not None and self.pnl.selected is not None):
            return self.pnl.selected
        else:
            pass

    def OnOk(self, evt):
        self.Close()
        pass

    def OnClose(self, evt):
        self.pnl.selected = list()
        self.Close()
        pass


if __name__ == "__main__":
    try:
        app = wx.PySimpleApp()
        selector = CtrSelector(None, -1)
        selector.ShowModal()
        selector.Destroy()
        print selector.GetSelected()
    except(KeyboardInterrupt, SystemExit):
        sys.exit()
