#-*- coding: utf-8 -*-
import unittest
import sys
import time
import json
import cloud_kitchen
from unittest.mock import MagicMock
from cloud_kitchen.cloud_kitchen import CloudKitchen
from cloud_kitchen.shelf_client.in_memory import InMemoryShelfClient
from cloud_kitchen.shelf_manager import ShelfManager
from cloud_kitchen.model.order import Order
from cloud_kitchen.model.shelf import Shelf
from config import *

OVERFLOW_SHELF='overflow'
SHELVES = [
    {
        "name" : "hot",
        "capacity" : 1,
        "decay_factor" : 1
    },
    {
        "name" : "overflow",
        "capacity" : 2,
        "decay_factor" : 2
    }
]

ORDERS = [
    {
      "name": "Pad See Ew",
      "temp": "hot",
      "shelfLife": 210,
      "decayRate": 0.72
    },
    {
      "name": "Hot Dog",
      "temp": "hot",
      "shelfLife": 375,
      "decayRate": 0.4
    }
]

def get_shelves_arr():
    shelves = []
    for shelf in Shelves:
        shelf_obj = Shelf(
            name=shelf['name'],
            capacity=shelf['capacity'],
            decay_factor=shelf['decay_factor'],
        )
    return shelves

def get_orders_arr():
    orders = []
    for e in ORDERS:
      order_obj = Order(
          name=e['name'],
          temp=e['temp'],
          shelf_life=e['shelfLife'],
          decay_rate=e['decayRate']
      )
      orders.append(order_obj)
    return orders


class CloudKitchenTestCase(unittest.TestCase):
    """ Test cases for cloud kitchen application
    """

    #@unittest.skip("Tested")
    def test_place_order(self):
        shelf_client = InMemoryShelfClient()
        shelf_manager = ShelfManager(
            shelf_client,
            SHELVES
        )
        # Execute kitchen
        kitchen = CloudKitchen(
            order_queue=MagicMock(),
            shelves=ShelfManager(
                shelf_client,
                SHELVES
            ),
            dispatcher=MagicMock(),
            collector=MagicMock()
        )
        orders = get_orders_arr()
        kitchen.process_order(orders[0])
        num_orders = len(kitchen.shelves.client.shelves[orders[0].temp])
        self.assertEqual(num_orders, 1)

    def test_pickup_order(self):
        shelf_client = InMemoryShelfClient()
        shelf_manager = ShelfManager(
            shelf_client,
            SHELVES
        )
        # Execute kitchen
        kitchen = CloudKitchen(
            order_queue=MagicMock(),
            shelves=ShelfManager(
                shelf_client,
                SHELVES
            ),
            dispatcher=MagicMock(),
            collector=MagicMock()
        )
        orders = get_orders_arr()
        kitchen.process_order(orders[0])
        kitchen.pickup_order(orders[0].id)
        num_orders = len(kitchen.shelves.client.shelves[orders[0].temp])
        self.assertEqual(num_orders, 0)


    def test_getting_shelves_state(self):
        shelf_client = InMemoryShelfClient()
        shelf_manager = ShelfManager(
            shelf_client,
            SHELVES
        )
        # Execute kitchen
        kitchen = CloudKitchen(
            order_queue=MagicMock(),
            shelves=ShelfManager(
                shelf_client,
                SHELVES
            ),
            dispatcher=MagicMock(),
            collector=MagicMock()
        )
        orders = get_orders_arr()
        for o in orders:
            kitchen.process_order(o)
        state = kitchen.get_state()
        self.assertEqual(len(state), 2)


if __name__ == '__main__':
    unittest.main()