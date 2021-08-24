from datetime import datetime
import pandas_datareader as web
import backtrader as bt 

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma = bt.ind.SMA(period=50)
        price = self.data
        crossover = bt.ind.CrossOver(price,sma)
        self.signal_add(bt.SIGNAL_LONG, crossover)

cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)

data = bt.feeds.YahooFinanceData(dataname='BTC-USD',fromdate=datetime(2015,1,1), todate=datetime(2021,1,1))

cerebro.adddata(data)
cerebro.run()
cerebro.plot()
