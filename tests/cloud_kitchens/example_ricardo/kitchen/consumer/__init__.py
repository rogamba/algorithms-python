from abc import ABCMeta

from .handler import NewOrderHandler
from ..model.order import Order


class OrderConsumer(metaclass=ABCMeta):
    """[summary]
    """
    def start_consuming(self, handler: NewOrderHandler):
        """[summary]

        :param handler: [description]
        :type handler: NewOrderHandler
        """
        raise NotImplementedError()


class OrderHandler(metaclass=ABCMeta):
    """[summary]
    """
    def handle(self, new_order: Order):
        """[summary]

        :param new_order: [description]
        :type new_order: Order
        """
        raise NotImplementedError()
