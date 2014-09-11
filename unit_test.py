
from trading.engine.order import Order
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

    def tearDown(self):
        pass



if __name__ == '__main__':
    cases = ['test_order',
             'test_match',
             'test_aggregate_match_bid_bigger_ask',
             'test_aggregate_match_bid_less_ask',
             'test_aggregate_match_bid_equal_ask']
    suite = unittest.TestSuite(map(TestInstrument, cases))
    unittest.TextTestRunner(verbosity=2).run(suite)