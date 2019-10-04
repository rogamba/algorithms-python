from abc import ABCMeta

from ..model.order import Order


class ShelfClient(metaclass=ABCMeta):
    """[summary]
    """
    def put(self, shelf_name: str, order: Order):
        """
        Try to put a new order in the shelve.

        :param shelve_name: The name of the shelf
        :param order: The order to put in the shelf
        """
        raise NotImplementedError()

    def pop_by_id(self, id: str) -> Order:
        """[summary]
        
        :param id: [description]
        :type id: str
        :return: [description]
        :rtype: Order
        """
        raise NotImplementedError()

    def get_size(self, shelf_name: str) -> int:
        """[summary]
        
        :param shelve_name: [description]
        :type shelve_name: str
        :return: [description]
        :rtype: int
        """
        raise NotImplementedError()

    def iterate_all_orders(self, shelf_name: str):
        """[summary]
        
        :param shelve_name: [description]
        :type shelve_name: str
        """
        raise NotImplementedError()
