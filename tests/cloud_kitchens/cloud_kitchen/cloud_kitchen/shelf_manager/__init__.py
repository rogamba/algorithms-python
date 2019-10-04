import threading
import json
from ..model.order import Order
from ..model.shelf import Shelf
from ..shelf_client import ShelfClient

OVERFLOW_SHELF = 'overflow'

class ShelfManager(object):
    """ Shelf manager class that uses a shelf client 
        to put, pop or move orders
    """
    def __init__(self, client: ShelfClient, shelves: list):
        self.client = client
        self.shelves = {}
        for shelf in shelves:
            shelf_obj = Shelf(
                name=shelf['name'],
                capacity=shelf['capacity'],
                decay_factor=shelf['decay_factor'],
            )
            self.shelves[shelf_obj.name] = shelf_obj
        if OVERFLOW_SHELF not in self.shelves:
            raise ValueError("Overflow shelf is needed!")

    def put(self, order: Order) -> bool:
        """ Add a new order to the shelf client
        
            :param order: 
            :type order: Order
            :return: bool, Ture if succeeded, False if there's not enough space
        """
        shelve = self.shelves.get(order.temp)
        if not shelve:
            raise ValueError("Invalid temp shelf found: {}".format(order.temp))

        lock = threading.Lock()
        with lock:
            shelve_name = shelve.name
            if self.client.get_size(shelve.name) >= shelve.capacity:
                shelve_name = OVERFLOW_SHELF
                if self.client.get_size(shelve_name) >= self.shelves.get(OVERFLOW_SHELF).capacity:
                    return False
            # Set oder decay factor depending on the shelf
            self.client.put(shelve_name, order)
        return True

    def pop_by_id(self, id: str) -> Order:
        """ Remove and order from the shelf given it's id
        
            :param id: 
            :type id: str
            :return: Order
            :rtype: Order
        """
        order = self.client.pop_by_id(id)
        if not order:
            return None
        self._rearrange_shelves()
        return order

    def _rearrange_shelves(self):
        """ If an overflow shelf exists among our shelves, try to
            rearrange orders to their permanent shelf
        """
        if OVERFLOW_SHELF in self.client.shelves:
            for order in self.client.iterate_all_orders(OVERFLOW_SHELF):
                self._try_to_move_to_permanent_shelf(order)

    def _try_to_move_to_permanent_shelf(self, order: Order):
        """ If an order is located in the overflow shelf, try to
            move it to it's corresponding shelf
        """
        lock = threading.Lock()
        with lock:
            if self._shelf_has_space(order.temp):
                self.client.pop_by_id(order.id)
                self.client.put(order.temp, order)

    def _shelf_has_space(self, shelf_name: str):
        """ Check if a given shelf has engough space

            :shelf_name: str
            :return: True or Flase
        """
        return self.client.get_size(
            shelf_name) < self.shelves[shelf_name].capacity

    def get_state(self):
        """ Get the state of all the shelves in a dictionary
            format

            :return: dictionary of the shelves and their orders
            :rtype: dict
        """
        shelves = {}
        lock = threading.Lock()
        for key, orders in self.client.shelves.items():
            shelves[key] = []
            for order in orders:
                shelves[key].append({
                    'id' : order.id,
                    'name' : order.name,
                    'temp' : order.temp,
                    'shelf_life' : order.shelf_life,
                    'decay_rate' : order.decay_rate,
                    'value' : order.compute_value(self.shelves[key].decay_factor),
                    'normalized_value' : order.normalized_value(self.shelves[key].decay_factor)
                })
        # Open and save file
        return shelves
