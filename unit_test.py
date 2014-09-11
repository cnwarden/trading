#!/usr/bin/python

from trading.engine.order import Order, OrderSide
from trading.engine.market import Market
from trading.engine.instrument import Instrument
import unittest

"""
unittest suite of trading module
"""

class TestInstrument(unittest.TestCase):
    """
    test instrument functions
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_order(self):
        instrument = Instrument(id='APPL')
        instrument.insert(Order(id=1, price=1.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=2, price=2.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=3, price=3.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=4, price=4.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=5, price=5.0, quantity=100, side=OrderSide.BUY))

    def test_match(self):
        instrument = Instrument(id='APPL')
        instrument.insert(Order(id=1, price=1.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=2, price=2.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=3, price=3.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=4, price=4.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=5, price=5.0, quantity=100, side=OrderSide.BUY))

        instrument.insert(Order(id=6, price=5.0, quantity=100, side=OrderSide.SELL))

        instrument.match()

    def test_aggregate_match_bid_bigger_ask(self):
        instrument = Instrument(id='APPL')
        instrument.insert(Order(id=4, price=4.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=3, price=2.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=1, price=3.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=2, price=5.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=5, price=5.0, quantity=200, side=OrderSide.BUY))
        instrument.insert(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY))

        instrument.insert(Order(id=6, price=5.0, quantity=200, side=OrderSide.SELL))

        instrument.match()

    def test_aggregate_match_bid_less_ask(self):
        instrument = Instrument(id='APPL')
        instrument.insert(Order(id=4, price=4.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=3, price=2.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=1, price=3.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=2, price=5.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=5, price=5.0, quantity=200, side=OrderSide.BUY))
        instrument.insert(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY))

        instrument.insert(Order(id=6, price=5.0, quantity=600, side=OrderSide.SELL))

        instrument.match()

    def test_aggregate_match_bid_equal_ask(self):
        instrument = Instrument(id='APPL')
        instrument.insert(Order(id=4, price=4.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=3, price=2.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=1, price=3.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=2, price=5.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=5, price=5.0, quantity=200, side=OrderSide.BUY))
        instrument.insert(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY))

        instrument.insert(Order(id=6, price=5.0, quantity=500, side=OrderSide.SELL))

        instrument.match()

    def test_orders_count_by_side(self):
        instrument = Instrument(id='APPL')
        instrument.insert(Order(id=4, price=4.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=3, price=2.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=1, price=3.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=2, price=5.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=5, price=5.0, quantity=200, side=OrderSide.BUY))
        instrument.insert(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY))

        self.assertEqual(6, instrument.get_orders_by_side(OrderSide.BUY))

        instrument.insert(Order(id=6, price=5.0, quantity=500, side=OrderSide.SELL))

        self.assertEqual(1, instrument.get_orders_by_side(OrderSide.SELL))

    def test_orders_count_total(self):
        instrument = Instrument(id='APPL')
        instrument.insert(Order(id=4, price=4.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=3, price=2.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=1, price=3.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=2, price=5.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=5, price=5.0, quantity=200, side=OrderSide.BUY))
        instrument.insert(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY))

        instrument.insert(Order(id=6, price=5.0, quantity=500, side=OrderSide.SELL))

        self.assertEqual(7, instrument.get_total_orders())


class TestMarket(unittest.TestCase):
    """
    test market behaviour
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_order_add(self):
        pass

    def test_order_add_multiple(self):
        pass

    def test_order_del(self):
        pass

    def test_lookup(self):
        pass


class TestCallback(unittest.TestCase):
    """
    test market trade/order callback
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_order_added(self):
        pass

    def test_order_changed(self):
        pass

    def test_order_removed(self):
        pass



if __name__ == '__main__':
    CASES = ['test_order',
             'test_match',
             'test_aggregate_match_bid_bigger_ask',
             'test_aggregate_match_bid_less_ask',
             'test_aggregate_match_bid_equal_ask',
             'test_orders_count_by_side',
             'test_orders_count_total']
    SUITE = unittest.TestSuite(map(TestInstrument, CASES))
    unittest.TextTestRunner(verbosity=2).run(SUITE)


    CASES = ['test_order_add',
             'test_order_add_multiple',
             'test_order_del',
             'test_lookup']
    SUITE = unittest.TestSuite(map(TestMarket, CASES))
    unittest.TextTestRunner(verbosity=2).run(SUITE)
