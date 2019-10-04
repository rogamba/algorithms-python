import threading

from . import ShelfClient
from ..model.order import Order


class InMemoryShelfClient(ShelfClient):
    """[summary]
    """
    def __init__(self):
        self.shelves = {}
        self.orders = {}

    def put(self, shelf_name: str, order: Order):
        """[summary]

        :param shelve_name: [description]
        :type shelve_name: str
        :param order: [description]
        :type order: Order
        """
        if shelf_name not in self.shelves:
            self.shelves[shelf_name] = []
        if order.id in self.orders:
            self.orders[order.id] = order
        else:
            self.orders[order.id] = order
            self.shelves[shelf_name].append(self.orders[order.id])

    def pop_by_id(self, id: str) -> Order:
        """[summary]

        :param id: [description]
        :type id: str
        :return: [description]
        :rtype: Order
        """
        with threading.Lock():
            if id not in self.orders:
                return None
            order_to_return = self.orders[id]
            self.shelves[order_to_return.temp.value].remove(order_to_return)
            del self.orders[id]
        return order_to_return

    def get_size(self, shelf_name: str) -> int:
        """[summary]

        :param shelve_name: [description]
        :type shelve_name: str
        :return: [description]
        :rtype: int
        """
        return len(self.shelves.get(shelf_name, []))

    def iterate_all_orders(self, shelf_name: str):
        """[summary]

        :param shelve_name: [description]
        :type shelve_name: str
        :raises ValueError: [description]
        """
        if shelf_name not in self.shelves:
            raise ValueError("Invalid shelf name: {}".format(shelf_name))
        for order in self.shelves[shelf_name]:
            yield order
