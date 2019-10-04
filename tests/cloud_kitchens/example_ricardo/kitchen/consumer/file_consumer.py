from .handler import NewOrderHandler
from . import OrderConsumer


class FileBasedOrderConsumer(OrderConsumer):
    def __init__(self, orders_file: str):
        pass

    def start_consuming(self, handler: NewOrderHandler):
        raise NotImplementedError()
