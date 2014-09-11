#!/usr/bin/python

import sys

class BasicTradingCallback(object):
    """
        simple callback class, work as NullCallback
    """

    def onTrade(self, instrument):
        pass

    def onOrderAdded(self, order, instrument):
        pass

    def onOrderChanged(self, order, instrument):
        pass

    def onOrderRemoved(self, order, instrument):
        pass

    

