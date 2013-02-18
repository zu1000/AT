import matplotlib
matplotlib.use('WXAgg')
import pylab
import matplotlib.dates
import matplotlib.finance
import matplotlib.backends.backend_wxagg as wxagg
    
import wx

'''
date1 = (2004, 2, 1)
date2 = (2004, 4, 12)

mondays = matplotlib.dates.WeekdayLocator(matplotlib.dates.MONDAY)
alldays = matplotlib.dates.DayLocator()
weekFormatter = matplotlib.dates.DateFormatter('%b %d')
dayFormatter = matplotlib.dates.DateFormatter('%d')

quotes = matplotlib.finance.quotes_historical_yahoo('INTC', date1, date2)
if len(quotes) == 0:
    raise SystemExit

fig = pylab.figure()
fig.subplots_adjust(bottom = 0.2)
ax = fig.add_subplot(111)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)

matplotlib.finance.candlestick(ax, quotes, width=0.6)
ax.xaxis_date()
ax.autoscale_view()
pylab.setp(pylab.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
pylab.show()
'''

class KFrame(wx.MDIChildFrame):
    def __init__(self, parent):
        wx.MDIChildFrame.__init__(self, parent, -1, "Demo")
        self.create_panel()
        
    def create_panel(self):
        self.panel = wx.Panel(self)
        
        self.create_plot()
        
        self.canvas = wxagg.FigureCanvasWxAgg(self.panel, -1, self.fig)

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.canvas, 1, flag=wx.LEFT | wx.TOP | wx.GROW, border=0)        
        self.panel.SetSizer(self.vbox)
        self.vbox.Fit(self)

        self.canvas.draw()
        
    def create_plot(self):
        self.fig = pylab.figure()
        self.fig.subplots_adjust(bottom = 0.2)
        
        self.date1 = (2004, 2, 1)
        self.date2 = (2004, 4, 12)

        self.mondays = matplotlib.dates.WeekdayLocator(matplotlib.dates.MONDAY)
        self.alldays = matplotlib.dates.DayLocator()
        self.weekFormatter = matplotlib.dates.DateFormatter('%b %d')
        self.dayFormatter = matplotlib.dates.DateFormatter('%d')

        self.quotes = matplotlib.finance.quotes_historical_yahoo('INTC', self.date1, self.date2)
        if len(self.quotes) == 0:
            raise SystemExit

        self.ax = self.fig.add_subplot(111)
        self.ax.xaxis.set_major_locator(self.mondays)
        self.ax.xaxis.set_minor_locator(self.alldays)
        self.ax.xaxis.set_major_formatter(self.weekFormatter)
        matplotlib.finance.candlestick(self.ax, self.quotes, width=0.6)
        self.ax.xaxis_date()
        self.ax.autoscale_view()
        pylab.setp(pylab.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

'''        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    app.frame = KFrame()
    app.frame.Show()
    app.MainLoop()
'''