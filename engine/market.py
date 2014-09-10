





import sys
from order import OrderSide


class Instrument(object):
    """docstring for Instrument"""
    def __init__(self, id=''):
        super(Instrument, self).__init__()

        self.id = id
        self.description = 'Apple Corporation'
        #key = price
        self.bidOrders = {}
        self.askOrders = {}

    def insert(self, order):
        if order.side == OrderSide.BUY:
            self.bidOrders[order.executedPrice] = [] if not self.bidOrders.has_key(order.executedPrice) else self.bidOrders[order.executedPrice]
            self.bidOrders[order.executedPrice] += [order]
        else:
            self.askOrders[order.executedPrice] = [] if not self.askOrders.has_key(order.executedPrice) else self.askOrders[order.executedPrice]
            self.askOrders[order.executedPrice] += [order]

    def erase(self, order):
        pass

    def find(self, order_id):
        pass

    def match(self):
        bidList = sorted(self.bidOrders.keys(), key=lambda x:-x)
        askList = sorted(self.askOrders.keys(), key=lambda x: x)

        #top bid and ask
        if len(bidList)>0 and len(askList)>0 and bidList[0] == askList[0]:

            executedPrice = bidList[0]

            total_bid_vol = sum([order.quantity for order in self.bidOrders[executedPrice]])
            total_ask_vol = sum([order.quantity for order in self.askOrders[executedPrice]])

            print '%d : %d' % (total_bid_vol, total_ask_vol)
            executedSize = min(total_bid_vol, total_ask_vol)

            #for order in self.bidOrders[bidList[0]]:
            def __dec_order(orderlist, remainSize):
                for order in orderlist:
                    if order.quantity > remainSize:
                        order.quantity -= remainSize
                        remainSize = 0
                        break
                    elif order.quantity < remainSize:
                        order.quantity = 0
                        remainSize -= order.quantity
                        continue
                    else:
                        order.quantity = 0
                        remainSize = 0

                    if remainSize == 0:
                        break

            __dec_order(self.bidOrders[bidList[0]], executedSize)
            __dec_order(self.askOrders[askList[0]], executedSize)

            self.bidOrders[executedPrice] = [order for order in self.bidOrders[executedPrice] if order.quantity >0 ]
            self.askOrders[executedPrice] = [order for order in self.askOrders[executedPrice] if order.quantity >0 ]

            if len(self.bidOrders[executedPrice]) == 0:
                del self.bidOrders[executedPrice]
            if len(self.askOrders[executedPrice]) == 0:
                del self.askOrders[executedPrice]


    def display(self):
        pass

    def __display_orderbook(self):

        outstr = '%30s|%-30s\n' % ('BID','ASK')

        sortedBid = sorted(self.bidOrders.keys(), key=lambda x:-x)
        sortedAsk = sorted(self.askOrders.keys(), key=lambda x: x)

        #detail orderbook

        for i in range(0, max(len(self.bidOrders), len(self.askOrders))):
            if i < min(len(self.bidOrders), len(self.askOrders)):
                bidOrders = self.bidOrders[sortedBid[i]]
                askOrders = self.askOrders[sortedAsk[i]]

                for j in range(0, max(len(bidOrders), len(askOrders))):
                    if j < min(len(bidOrders), len(askOrders)):
                        bid = bidOrders[j]
                        ask = askOrders[j]
                        outstr += '%10d%10f%10d|%10d%10f%10d\n' % (bid.id, bid.executedPrice, bid.quantity,
                                                                   ask.id, ask.executedPrice, ask.quantity)
                    elif j >= len(bidOrders):
                        # exceed is ASK
                        for m in range(j, len(askOrders)):
                            ask = askOrders[m]
                            outstr += '%s|%10d%10f%10d\n' % (' ' * 30,
                                                             ask.id, ask.executedPrice, ask.quantity )
                        break
                    elif j >= len(askOrders):
                        # exceed is BID
                        for m in range(j, len(bidOrders)):
                            bid = bidOrders[m]
                            outstr += '%10d%10f%10d|%s\n' % (bid.id, bid.executedPrice, bid.quantity,
                                                             ' ' * 30 )
                        break

            elif i >= len(self.bidOrders):
                # Ask side
                askOrders = self.askOrders[sortedAsk[i]]
                for m in range(0, len(askOrders)):
                    ask = askOrders[m]
                    outstr += '%s|%10d%10f%10d\n' % (' ' * 30,
                                                     ask.id, ask.executedPrice, ask.quantity )
            elif i >= len(self.askOrders):
                # Bid side
                bidOrders = self.bidOrders[sortedBid[i]]
                for m in range(0, len(bidOrders)):
                    bid = bidOrders[m]
                    outstr += '%10d%10f%10d|%s\n' % (bid.id, bid.executedPrice, bid.quantity,
                                                     ' ' * 30 )

            outstr += '-' * 60
            outstr += '\n'

        return outstr

    def __str__(self):
        outstr = 'ID:%s\n' % (self.id)
        outstr = outstr + 'Description:%s\n' % (self.description)
        outstr = outstr + self.__display_orderbook()
        return outstr




class Market(object):
    """docstring for Market"""
    def __init__(self):
        super(Market, self).__init__()

    def insert(self, order):
        pass

    def erase(self, order):
        pass

    def find(self, order_id):
        pass

    def display(self):
        pass


    def __match(self, bidorder, askorder):
        pass


