#!/usr/bin/python

import datetime

class Trade(object):

    def __init__(self, id=None, price=0.0, volume=0.0):
        self.volume = volume
        self.price = price

        self.id = id
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return 'TradeID:%s Price:%f Volume:%d' % (self.id, self.price, self.volume)
