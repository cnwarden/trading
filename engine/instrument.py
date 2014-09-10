#!/usr/bin/python

import sys
from order import OrderSide
from callback import BasicTradingCallback


class Instrument(object):
    """docstring for Instrument"""
    def __init__(self, id='', callback=BasicTradingCallback()):
        super(Instrument, self).__init__()

        self.id = id
        self.description = 'Apple Corporation'
        #key = price
        self.bidOrders = {}
        self.askOrders = {}

        self.callback = callback

    def insert(self, order):
        if order.side == OrderSide.BUY:
            self.bidOrders[order.executedPrice] = [] if not self.bidOrders.has_key(order.executedPrice) else self.bidOrders[order.executedPrice]
            self.bidOrders[order.executedPrice] += [order]
        else:
            self.askOrders[order.executedPrice] = [] if not self.askOrders.has_key(order.executedPrice) else self.askOrders[order.executedPrice]
            self.askOrders[order.executedPrice] += [order]

    def erase(self, order_id):

        def __erase_bidask(sideOrders):
            for item in sideOrders.iteritems():
                for i, order in enumerate(item[1]):
                    if order.id == order_id:
                        del item[1][i]
                        if not item[1]:
                            del sideOrders[item[0]]
                            if callable(getattr(self.callback, 'onOrderRemoved')):
                                self.callback.onOrderChanged(order)
                        return

        __erase_bidask(self.bidOrders)
        __erase_bidask(self.askOrders)


    def get_orders_by_side(self, side):
        total = 0
        if side == OrderSide.BUY:
            for orderlist in self.bidOrders.itervalues():
                total += len(orderlist)
        else:
            for orderlist in self.askOrders.itervalues():
                total += len(orderlist)
        return total


    def get_total_orders(self):
        return self.get_orders_by_side(OrderSide.BUY) + self.get_orders_by_side(OrderSide.SELL)

    def find(self, order_id):
        for orderList in self.bidOrders.itervalues():
            for order in orderList:
                if order.id == order_id:
                    return order
        for orderList in self.askOrders.itervalues():
            for order in orderList:
                if order.id == order_id:
                    return order
        return None

    def match(self):
        bidList = sorted(self.bidOrders.keys(), key=lambda x:-x)
        askList = sorted(self.askOrders.keys(), key=lambda x: x)

        #top bid and ask
        if len(bidList)>0 and len(askList)>0 and bidList[0] == askList[0]:

            executedPrice = bidList[0]

            total_bid_vol = sum([order.quantity for order in self.bidOrders[executedPrice]])
            total_ask_vol = sum([order.quantity for order in self.askOrders[executedPrice]])

            executedSize = min(total_bid_vol, total_ask_vol)

            #for order in self.bidOrders[bidList[0]]:
            def __dec_order(orderlist, remainSize):
                for order in orderlist:
                    if order.quantity > remainSize:
                        order.quantity -= remainSize
                        remainSize = 0
                        if callable(getattr(self.callback, 'onOrderChanged')):
                            self.callback.onOrderChanged(order)
                        break
                    elif order.quantity < remainSize:
                        order.quantity = 0
                        remainSize -= order.quantity
                        if callable(getattr(self.callback, 'onOrderChanged')):
                            self.callback.onOrderChanged(order)
                        continue
                    else:
                        order.quantity = 0
                        remainSize = 0
                        if callable(getattr(self.callback, 'onOrderChanged')):
                            self.callback.onOrderChanged(order)

                    if remainSize == 0:
                        break

            __dec_order(self.bidOrders[bidList[0]], executedSize)
            __dec_order(self.askOrders[askList[0]], executedSize)

            #top orders generate trade
            if callable(getattr(self.callback, 'onTrade')):
                self.callback.onTrade()

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

