from .model.order import Order
from .consumer import OrderHandler
from .kitchen import Kitchen


class NewOrderHandler(OrderHandler):
    """[summary]
    """
    def __init__(self, kitchen: Kitchen):
        self.kitchen = kitchen

    def handle(self, new_order: Order):
        """[summary]

        :param new_order: [description]
        :type new_order: Order
        """
        self.kitchen.pickup_order(new_order)
