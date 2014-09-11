#!/usr/bin/python

from engine.order import Order, OrderSide
from engine.market import Market
from engine.instrument import Instrument
from engine.callback import BasicTradingCallback
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
        self.market = Market()
        self.instrument = Instrument('APPL')

        self.market.add_instrument(self.instrument)

    def tearDown(self):
        pass

    def test_order_add(self):
        #reassign the order id when add
        self.market.add(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')
        order = self.market.lookup(1)

        self.assertEqual(order.id, 1)

    def test_order_add_multiple(self):
        self.market.add(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')
        self.market.add(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')
        self.market.add(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')
        self.market.add(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')
        self.market.add(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')
        self.market.add(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')

        order = self.market.lookup(6)

        self.assertEqual(order.id, 6)

    def test_order_del(self):
        self.market.add(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')
        self.market.erase(1)
        order = self.market.lookup(1)

        self.assertEqual(order, None)

    def test_lookup(self):
        self.market.add(Order(id=1, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')
        order = self.market.lookup(1)

        self.assertEqual(order.id, 1)


class MyCallback(BasicTradingCallback):
    def onTrade(self, instrument):
        pass

    def onOrderAdded(self, order, instrument):
        self.trigged_add = True

    def onOrderChanged(self, order, instrument):
        self.trigged_change = True

    def onOrderRemoved(self, order, instrument):
        self.trigged_remove = True

    def reset(self):
        self.trigged_add    = True
        self.trigged_change = True
        self.trigged_remove = True


class TestCallback(unittest.TestCase):
    """
    test market trade/order callback
    """
    def setUp(self):
        self.market = Market()
        self.policy = MyCallback()
        self.policy.reset()
        self.instrument = Instrument('APPL', callback=self.policy)

        self.market.add_instrument(self.instrument)

    def tearDown(self):
        pass

    def test_order_added(self):
        self.market.add(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')
        order = Order(id=7, price=5.0, quantity=200, side=OrderSide.SELL)
        self.market.add(order, 'APPL')
        
        self.assertEqual(True, self.policy.trigged_add)

    def test_order_changed(self):
        self.market.add(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')
        order = Order(id=7, price=5.0, quantity=200, side=OrderSide.SELL)
        self.market.add(order, 'APPL')

        self.assertEqual(True, self.policy.trigged_change)

    def test_order_removed(self):
        self.market.add(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY), 'APPL')
        order = Order(id=7, price=5.0, quantity=200, side=OrderSide.SELL)
        self.market.add(order, 'APPL')

        self.assertEqual(True, self.policy.trigged_remove)



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

    CASES = ['test_order_added',
             'test_order_changed',
             'test_order_removed']
    SUITE = unittest.TestSuite(map(TestCallback, CASES))
    unittest.TextTestRunner(verbosity=2).run(SUITE)

