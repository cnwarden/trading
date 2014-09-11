

from trading.server.udpserver import *
from trading.engine.order import *
from trading.engine.market import *
from trading.engine.instrument import *

import unittest

class TestInstrument(unittest.TestCase):

    def setUp(self):
        pass

    def test_startup(self):
        server = UdpServer()
        server.open()
        for i in xrange(10):
            server.send('testing')
        server.close()


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

        print instrument
        
        instrument.match()

        print instrument
        
    def test_aggregate_match_bid_less_ask(self):
        instrument = Instrument(id='APPL')
        instrument.insert(Order(id=4, price=4.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=3, price=2.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=1, price=3.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=2, price=5.0, quantity=100, side=OrderSide.BUY))
        instrument.insert(Order(id=5, price=5.0, quantity=200, side=OrderSide.BUY))
        instrument.insert(Order(id=7, price=5.0, quantity=200, side=OrderSide.BUY))


        instrument.insert(Order(id=6, price=5.0, quantity=600, side=OrderSide.SELL))

        print instrument
        
        instrument.match()

        print instrument

    def tearDown(self):
        pass



if __name__ == '__main__':
    cases = ['test_order']
    suite = unittest.TestSuite(map(TestInstrument, cases))
    unittest.TextTestRunner(verbosity=2).run(suite)