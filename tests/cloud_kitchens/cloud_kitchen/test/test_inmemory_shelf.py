#-*- coding: utf-8 -*-
import unittest
import sys
import time
import json
import cloud_kitchen
from cloud_kitchen.shelf_client.in_memory import InMemoryShelfClient
from cloud_kitchen.model.order import Order
from cloud_kitchen.model.shelf import Shelf
from config import *

SHELVES = [
    {
        "name" : "hot",
        "capacity" : 15,
        "decay_factor" : 1
    },
    {
        "name" : "overflow",
        "capacity" : 20,
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
        "name": "McFlury",
        "temp": "frozen",
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


class InMemoryShelfClientTestCase(unittest.TestCase):
    """ Test cases for in-memory shelf client
    """
    #@unittest.skip("Tested")
    def test_place_order_in_shelf(self):
        # Initialize shelves
        pass

    #@unittest.skip("Tested")
    def test_put_new_order_in_shelf(self):
        orders = get_orders_arr()
        shelf_client = InMemoryShelfClient()
        shelf_client.put(
          orders[0].temp,
          orders[0] 
        )
        # Assert shelf length
        num_orders = len(shelf_client.shelves[orders[0].temp])
        self.assertGreater(num_orders, 0)

    #@unittest.skip("Tested")
    def test_pop_order_from_shelf_by_id(self):
        orders = get_orders_arr()
        shelf_client = InMemoryShelfClient()
        shelf_client.put(
          orders[0].temp,
          orders[0] 
        )
        shelf_client.pop_by_id(orders[0].id)
        num_orders = len(shelf_client.shelves[orders[0].temp])
        self.assertEqual(num_orders, 0)

    #@unittest.skip("Tested")
    def test_iterate_orders_on_shelf(self):
        orders = get_orders_arr()
        shelf_client = InMemoryShelfClient()
        for order in orders:
            shelf_client.put(
                order.temp,
                order 
            )
        num_orders = len(shelf_client.shelves[orders[0].temp])
        c = 0
        for o in shelf_client.iterate_all_orders(orders[0].temp):
            c+=1
        self.assertEqual(num_orders, c)


if __name__ == '__main__':
    unittest.main()