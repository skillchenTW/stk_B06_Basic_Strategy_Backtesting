import backtrader as bt
from backtrader import position

class BuyHold(bt.Strategy):

    def next(self):
        if self.position.size == 0:
            size = int(self.broker.getcash() / self.data)
            self.buy(size=size)