from abc import ABCMeta

from ..model.order import Order


class ShelfClient(metaclass=ABCMeta):

    def put(self, shelf_name: str, order: Order):
        """Try to put a new order in the shelve.

        :param shelve_name: The name of the shelf
        :param order: The order to put in the shelf
        """
        raise NotImplementedError()

    def pop_by_id(self, id: str) -> Order:
        """Retrieve order given its id
        
        :param id: [description]
        :type id: str
        :return: [description]
        :rtype: Order
        """
        raise NotImplementedError()

    def get_size(self, shelf_name: str) -> int:
        """Get the current size by the shelve's name
        
        :param shelve_name: [description]
        :type shelve_name: str
        :return: [description]
        :rtype: int
        """
        raise NotImplementedError()

    def iterate_all_orders(self, shelf_name: str):
        """Iterator to retrieve all orders given
            a shelf name
        
        :param shelve_name: [description]
        :type shelve_name: str
        """
        raise NotImplementedError()
