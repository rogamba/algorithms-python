from . import OrderQueue
from threading import Thread
from collections import deque
from ..model.order import Order
import time

class InMemoryOrderQueue(OrderQueue):
    def __init__(self, handler=None):
        """ Initialize the in memory queue
        """ 
        self.orders = deque()
        self.handler = handler
        self.thread = Thread(target=self._watch)

    def set_handler(self, handler):
        """ Define handler to use to process orders
            :handler: function to use to process the order
        """
        self.handler = handler

    def watch(self):
        """ Check if thread is alive and start consuming
            new orders
        """
        if self.thread.isAlive():
            return
        self.thread.start()

    def _watch(self):
        """ Start watching queue in new thread  
        """
        while True:
            # Check if there's new order
            if len(self.orders) > 0:
                # Create a new order object
                e = self.orders.pop()
                order = Order(
                    name=e['name'],
                    temp=e['temp'],
                    shelf_life=e['shelfLife'],
                    decay_rate=e['decayRate']
                )
                # Handle
                self.handler(order)
