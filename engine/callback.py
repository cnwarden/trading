#!/usr/bin/python

import sys

class BasicTradingCallback(object):
    """
        simple callback class, work as NullCallback
    """

    def onTrade(self):
        pass

    def onOrderChanged(self, order):
        pass

    def onOrderRemoved(self, order):
        pass

    

