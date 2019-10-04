from threading import Thread, Lock
from . import Dispatcher
from ..model.order import Order
from ..shelf_client import ShelfClient
import time
import random
import logging

LOG = logging.getLogger(__name__)

class DriverDispatcher(Dispatcher):
    
    def __init__(
        self, 
        shelve_client: ShelfClient
    ):
        self.client = shelve_client
        self.thread = Thread(target=self._start_dispatching)

    def dispatch(self, order: Order):
        """ Stamp the order object with the dispatch time
            :order: Order object reference
        """ 
        order.pickup_time = time.time() + random.randint(2,10)
        return True

    def set_handler(self, handler):
        """ Set handler for piching up order
        """
        self.handler = handler

    def start_dispatching(self):
        """Start dispatcher execution
        """
        if self.thread.isAlive():
            return
        self.thread.start()

    def _start_dispatching(self):
        while True:
            for name in self.client.shelves:
                # Loop shelves and check order pickup time
                for order in self.client.iterate_all_orders(name):
                    if hasattr(order,'pickup_time') and time.time() > order.pickup_time:
                        order = self.handler(order.id)
                        LOG.info("Order {} picked up".format(order.id))
            time.sleep(0.1)
    


