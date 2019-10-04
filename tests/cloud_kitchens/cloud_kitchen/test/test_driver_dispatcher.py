#-*- coding: utf-8 -*-
import unittest
import sys
import time
import json
import cloud_kitchen
from cloud_kitchen.dispatcher.driver_dispatcher import DriverDispatcher
from cloud_kitchen.model.order import Order
from cloud_kitchen.model.shelf import Shelf
from config import *

ORDERS = [
    {
        "name": "Pad See Ew",
        "temp": "hot",
        "shelfLife": 210,
        "decayRate": 0.72
    },
    {
        "name": "McFlury",
        "temp": "frozen",
        "shelfLife": 375,
        "decayRate": 0.4
    }
]


class DriverDispatcherTestCase(unittest.TestCase):
    """ Test Case for Driver Dispatcher model
    """

    def test_stamp_pickup_order(self):
        dd = DriverDispatcher(None)
        order = Order(
            name=ORDERS[0]['name'],
            temp=ORDERS[0]['temp'],
            shelf_life=ORDERS[0]['shelfLife'],
            decay_rate=ORDERS[0]['decayRate']
        )
        dd.dispatch(order)
        self.assertTrue(hasattr(order,'pickup_time'))


if __name__ == '__main__':
    unittest.main()