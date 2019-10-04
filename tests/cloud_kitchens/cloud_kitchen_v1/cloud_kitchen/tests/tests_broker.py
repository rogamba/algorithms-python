#-*- coding: utf-8 -*-
import unittest
import config
import sys
import time
import json
import cloud_kitchen
from cloud_kitchen.models.broker import Broker
from collections import deque

class BrokerTestCase(unittest.TestCase):
    """ Test Case for Broker model
    """

    def setUp(self):
        """ Set up
        """
        pass

    def test_order_placement_rate(self):
        """ Testing timestamp for placing orders
            with a Poisson distribution given an 
            avg of 3.25 orders per second
        """ 
        broker = Broker(queue=deque(), avg_rate=config.INCOMMING_ORDERS_RATE)
        # Validate average delta of orders (3.5)
        delta = config.INCOMMING_ORDERS_RATE
        avg_time_between_orders = 1/delta
        stamp_detlas = []
        # Deltas
        for i in range(len(broker.orders)-2):
            stamp_detlas.append(
                (broker.orders[i+1]['placement_stamp']-broker.orders[i]['placement_stamp'])/1000
            )
        # Average delta
        avg_delta = sum(stamp_detlas)/len(stamp_detlas)
        # Acceptable error
        error = abs(avg_time_between_orders-avg_delta)
        self.assertTrue(error<=0.2)


    @unittest.skip("Smoke test")
    def test_simulation(self):
        """ Testing Broker place_order
        """ 
        broker = Broker(queue=deque(), avg_rate=config.INCOMMING_ORDERS_RATE)
        broker.simulate_placement()
        self.assertTrue(True)


    #@unittest.skip("Tested")
    def test_02_place_order(self):
        """ Testing Broker place_order
        """ 
        broker = Broker(queue=deque())
        result = broker.place_new_order(
            broker.orders[0]
        )
        print(broker.queue)
        self.assertTrue(len(broker.queue) > 0)


if __name__ == '__main__':
    unittest.main()
 