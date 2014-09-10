#!/usr/bin/python

import sys
import datetime

class OrderSide(object):
    BUY  = 0
    SELL = 1

class OrderType(object):
    MARKET = 0
    LIMIT  = 1


class Order(object):

    def __init__(self, id=None, price=0.0, quantity=0.0, side=OrderSide.BUY, type=OrderType.LIMIT):
        self.quantity = quantity
        self.executedQuantity = 0
        self.executedPrice = price
        self.side = side
        self.type = type

        self.id = id
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return 'OrderID:%s Price:%f Quantity:%d' % (self.id, self.executedPrice, self.quantity)
