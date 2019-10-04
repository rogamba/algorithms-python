import threading
from . import ShelfClient
from ..model.order import Order


class InMemoryShelfClient(ShelfClient):
    """[summary]
    """
    def __init__(self):
        self.shelves = {}
        self.orders = {}
        self.order_to_shelf = {}

    def __str__(self):
        s = ''
        for k in self.shelves:
            s+="{} : {}\n".format(k,len(self.shelves[k]))
        return s

    def get_current_shelf(self, order_id:str) -> str:
        """ Get the current shelf where and order resides
            :order_id: str
            :return: name of the shelf
        """
        return self.order_to_shelf[order_id]

    def put(self, shelf_name: str, order: Order):
        """ Try to put a new order in the shelve.

            :param shelve_name: [description]
            :type shelve_name: str
            :param order: [description]
            :type order: Order
        """
        with threading.Lock():
            if shelf_name not in self.shelves:
                self.shelves[shelf_name] = []
            if order.id in self.orders:
                self.orders[order.id] = order
            else:
                self.orders[order.id] = order
                self.shelves[shelf_name].append(self.orders[order.id])
            # Set order to shelf
            self.order_to_shelf[order.id] = shelf_name

    def pop_by_id(self, id: str) -> Order:
        """ Retrieve order given its id

            :param id: [description]
            :type id: str
            :return: [description]
            :rtype: Order
        """
        with threading.Lock():
            if id not in self.orders:
                return None
            order_to_return = self.orders[id]
            # Remove from the shelf that is currently located
            self.shelves[
                self.get_current_shelf(id)
            ].remove(order_to_return)
            del self.orders[id]
        return order_to_return

    def get_size(self, shelf_name: str) -> int:
        """ Get the current size by the shelve's name

            :param shelve_name: [description]
            :type shelve_name: str
            :return: [description]
            :rtype: int
        """
        return len(self.shelves.get(shelf_name, []))

    def iterate_all_orders(self, shelf_name: str):
        """ Iterator to retrieve all orders given
            a shelf name

            :param shelve_name: [description]
            :type shelve_name: str
            :raises ValueError: [description]
        """
        if shelf_name not in self.shelves:
            raise ValueError("Invalid shelf name: {}".format(shelf_name))
        for order in self.shelves[shelf_name]:
            yield order
