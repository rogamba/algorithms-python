from abc import ABCMeta

from . import NewOrderHandler


class OrderConsumer(metaclass=ABCMeta):
    def start_consuming(self, handler: NewOrderHandler):
        raise NotImplementedError()
