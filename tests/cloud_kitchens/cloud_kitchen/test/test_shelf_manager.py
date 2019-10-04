#-*- coding: utf-8 -*-
import unittest
import sys
import time
import json
import cloud_kitchen
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


class ShelfManagerTestCase(unittest.TestCase):
    """ Test cases for shelf manager
    """

    #@unittest.skip("Tested")
    def test_setup_shelves_objects(self):
        shelf_client = InMemoryShelfClient()
        shelf_manager = ShelfManager(
            shelf_client,
            SHELVES
        )
        self.assertEqual(len(SHELVES), len(shelf_manager.shelves))

    #@unittest.skip("Tested")
    def test_put_order_in_shelf(self):
        shelf_client = InMemoryShelfClient()
        orders = get_orders_arr()
        shelf_manager = ShelfManager(
            shelf_client,
            SHELVES
        )
        shelf_manager.put(orders[0])
        num_orders = len(shelf_manager.client.shelves[orders[0].temp])
        self.assertEqual(num_orders,1)

    #@unittest.skip("Tested")
    def test_pop_order_from_shelf_by_id(self):
        shelf_client = InMemoryShelfClient()
        orders = get_orders_arr()
        shelf_manager = ShelfManager(
            shelf_client,
            SHELVES
        )
        shelf_manager.put(orders[0])
        shelf_manager.pop_by_id(orders[0].id)
        num_orders = len(shelf_manager.client.shelves[orders[0].temp])
        self.assertEqual(num_orders, 0)

    #@unittest.skip("Tested")
    def test_put_order_on_overflow_shelf(self):
        shelf_client = InMemoryShelfClient()
        orders = get_orders_arr()
        shelf_manager = ShelfManager(
            shelf_client,
            SHELVES
        )
        for order in orders:
            shelf_manager.put(order)
        num_overflow = len(shelf_manager.client.shelves[OVERFLOW_SHELF])
        self.assertEqual(num_overflow,1)

    #@unittest.skip("Tested")
    def test_reorder_shelves(self):
        shelf_client = InMemoryShelfClient()
        orders = get_orders_arr()
        shelf_manager = ShelfManager(
            shelf_client,
            SHELVES
        )
        for order in orders:
            shelf_manager.put(order)
        # Remove from the permanente
        shelf_manager.client.pop_by_id(orders[0].id)
        # Move from overflow to permanent
        shelf_manager._rearrange_shelves()
        num_permanent = len(shelf_manager.client.shelves[orders[1].temp])
        self.assertEqual(num_permanent,1)

    #@unittest.skip("Tested")
    def test_put_order_fail_due_to_overflow(self):
        shelf_client = InMemoryShelfClient()
        orders = get_orders_arr()
        shelf_manager = ShelfManager(
            shelf_client,
            SHELVES
        )
        # Trying to put 4 orders
        for order in orders:
            shelf_manager.put(order)
        orders = get_orders_arr()
        for order in orders:
            shelf_manager.put(order)
        total_orders = sum([len(shelf_manager.client.shelves[k]) for k in shelf_manager.shelves.keys()])
        self.assertEqual(total_orders,3)



if __name__ == '__main__':
    unittest.main()