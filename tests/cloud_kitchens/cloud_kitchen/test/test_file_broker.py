#-*- coding: utf-8 -*-
import unittest
import sys
import time
import json
import cloud_kitchen
from cloud_kitchen.broker.file_broker import FileBasedBroker
from collections import deque
from config import *


class FileBasedBrokerTestCase(unittest.TestCase):
    """ Test Case for Broker model
    """

    def test_order_placement_rate(self):
        """ Testing timestamp for placing orders
            with a Poisson distribution given an 
            avg of 3.25 orders per second
        """ 
        broker = FileBasedBroker(
            filename=BROKER_FILE, 
            queue=deque(),
            incomming_rate=INCOMMING_ORDERS_RATE
        )
        # Validate average delta of orders (3.5)
        delta = INCOMMING_ORDERS_RATE
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
        broker = FileBasedBroker(
            filename=BROKER_FILE, 
            queue=deque(),
            incomming_rate=INCOMMING_ORDERS_RATE
        )
        broker._simulate()
        self.assertTrue(True)

    @unittest.skip("Tested")
    def test_02_place_order(self):
        """ Testing Broker place_order
        """ 
        broker = FileBasedBroker(
            filename=BROKER_FILE, 
            queue=deque(),
            incomming_rate=INCOMMING_ORDERS_RATE
        )
        result = broker.place_new_order(
            broker.orders[0]
        )
        print(broker.queue)
        self.assertTrue(len(broker.queue) > 0)


if __name__ == '__main__':
    unittest.main()
 