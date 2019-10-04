import threading

from .model.order import Order
from .shelf_client import ShelfClient

OVERFLOW_SHELF = 'overflow'


class ShelfManager(object):
    """[summary]
    """
    def __init__(self, client: ShelfClient, shelves: list):
        self.client = client
        self.shelves = {}
        for shelve in shelves:
            self.shelves[shelve.name] = shelve
        if OVERFLOW_SHELF not in self.shelves:
            raise ValueError("Overflow shelf is needed!")

    def put(self, order: Order) -> bool:
        """[summary]
        
        :param order: [description]
        :type order: Order
        :raises ValueError: [description]
        :return: [description]
        :rtype: bool
        """
        shelve = self.shelves.get(order.temp.value)
        if not shelve:
            raise ValueError("Invalid temp shelf found: {}".format(order.temp))

        lock = threading.Lock()
        with lock:
            shelve_name = shelve.name
            if self.client.get_size(shelve.name) >= shelve.capacity:
                shelve_name = OVERFLOW_SHELF
                if self.client.get_size(shelve_name) >= shelve.capacity:
                    #TODO: log and drop order
                    return False
            self.client.put(shelve_name, order)
        return True

    def pop_by_id(self, id: str) -> Order:
        """[summary]
        
        :param id: [description]
        :type id: str
        :return: [description]
        :rtype: Order
        """
        order = self.client.pop_by_id(id)
        if not order:
            return None
        self._rearrange_shelves()
        return order

    def _rearrange_shelves(self):
        for order in self.client.iterate_all_orders(OVERFLOW_SHELF):
            self._try_to_move_to_permanent_shelf(order)

    def _try_to_move_to_permanent_shelf(self, order: Order):
        lock = threading.Lock()
        with lock:
            if self._shelf_has_space(order.shelve_name):
                self.client.pop_by_id(order.id)
                self.client.put(self._get_shelf_name(order), order)

    def _get_shelf_name(self, order: Order) -> str:
        return order.temp.value

    def _shelf_has_space(self, shelf_name: str):
        return self.client.get_size(
            shelf_name) < self.shelves[shelf_name].capacity
