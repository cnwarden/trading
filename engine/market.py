#!/usr/bin/python

import sys

class Market(object):
    """docstring for Market"""
    def __init__(self):
        super(Market, self).__init__()

        self.orderLookupTbl = {}
        self.instrLookupTbl = {}
        self.gOrderId = 0

    def __generated_orderId(self):
        self.gOrderId += 1
        return self.gOrderId

    def add_instrument(self, instrument):
        self.instrLookupTbl[instrument.id] = instrument

    def add(self, order, instrument_id):
        """
            add an order in the instrument
        """
        if self.instrLookupTbl.has_key(instrument_id):
            order.id = self.__generated_orderId()
            self.orderLookupTbl[order.id] = self.instrLookupTbl[instrument_id]
            self.instrLookupTbl[instrument_id].insert(order)
        else:
            raise ValueError('invaild order for non-existed instrument id')

    def erase(self, order_id):
        if self.orderLookupTbl.has_key(order_id):
            # del in instrument
            self.orderLookupTbl[order_id].erase(order_id)
            del self.orderLookupTbl[order_id]
            

    def lookup(self, order_id):
        instrument = self.orderLookupTbl[order_id] if self.orderLookupTbl.has_key(order_id) else None
        if instrument != None:
            return instrument.find(order_id)

    def match(self, order):
        if self.orderLookupTbl.has_key(order.id):
            self.orderLookupTbl[order.id].match()

    def display(self):
        pass

