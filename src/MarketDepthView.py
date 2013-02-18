import wx
import wx.lib.agw.hypertreelist as HTL
import sys

import Network
import MDEvent

class MarketDepthView(HTL.HyperTreeList):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, 
                 size = wx.DefaultSize, style=wx.SUNKEN_BORDER, 
                 agwStyle=wx.TR_HAS_VARIABLE_ROW_HEIGHT | wx.TR_HIDE_ROOT | wx.TR_NO_LINES | wx.TR_ROW_LINES | wx.TR_COLUMN_LINES, 
                 log=None):
        HTL.HyperTreeList.__init__(self, parent, id, pos, size, style, agwStyle)

        #Create dictionary for contract item
        self.children = {} 
        self.CreateColumn()
        #self.StartMDService()

    def StartMDService(self):
        service = Network.MDService( ("localhost", 19999), self )
        service.daemon = True
        service.start()
        MDEvent.EVT_MD(self, self.HandleData)

    def CreateColumn(self):
        self.AddColumn("Contract")
        self.AddColumn("BidQ");
        self.AddColumn("Bid");
        self.AddColumn("Ask");
        self.AddColumn("AskQ");
        self.AddColumn("Open");
        self.AddColumn("High");
        self.AddColumn("Low");
        self.AddColumn("Close");
        self.SetMainColumn(0);
        self.SetColumnWidth(0, 175);

        #This will be hidden
        self.root = self.AddRoot("DUMMY ROOT");

    def AddContract(self, name):
        if name in self.children :
            pass
        child = self.AppendItem(self.root, name)
        last = self.AppendItem(child, "")
        self.children[name] = child
        # From this point, we need to get the market info
        self.SetItemText(child, "1000", 1)
        self.SetItemText(last, "2000", 1)

    def HandleData(self, event):
        print event.data


if __name__ == "__main__":
    try:
        app = wx.PySimpleApp()
        frame = wx.Frame(None, -1, "Test")
        view = MarketDepthView(frame)
        view.AddContract("Gold")
        view.AddContract("Silver")
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(view, 1, wx.EXPAND)
        frame.SetSizer(vbox)
        frame.Show()
        app.MainLoop()
    except(KeyboardInterrupt, SystemExit):
        sys.exit()
