from driver_dispatcher import DriverDispatcher
from order_consumer import OrderConsumer
from waste_collector import WasteCollecetor

from collections import deque
from threading import Lock, Thread
from cloud_kitchen.models.order import Order
import sys
import logging

logger = logging.getLogger(__name__)

class Kitchen(Object):
    """ Cloud Kitchen main application object
        :broker
        :order
        :waste_collector
    """
    def __init__(self, driver_dispatcher, order_consumer, waste_colector, broker):
        self.driver_dispatcher = driver_dispatcher
        self.order_consumer = order_consumer
        self.order_consumer.start_consuming(self.process_order)
        self.waste_colector = waste_colector()
        self.waste_colector.start_collecting()
        # Orders queue
        self.orders = deque()
        self.shelves = {
            "hot" : None,
            "cold" : None,
            "frozen" : None,
            "overflow" : None
        }
        # Start broker publisher
        self.broker=broker(queue=self.orders)
        self.start_broker()
        # Start watching orders
        self.watch_incomming_orders()
        # Start waste collector
        self.threads = {}

    def start_broker(self):
        """ Start broker simulator that publishes to
            orders queue
        """
        self.threads['broker'] = Thread(
            target=self.broker.simulate_placement()
        )


    def watch_incomming_orders(self):
        """ Start broker in new thread  
            Infinite loop watching the orders
        """
        try:
            while True:
                # Check if there's new order
                if len(self.orders) > 0:
                    self.process_order(self.pop())
        except Exception as e:
            logger.error(e)
            sys.exit()
    
    def process_order(self, order_element):
        """ Sent as callback to the broker?
        """
        # Create order object
        order = Order(order_element)
        # Place in correct shelf
        self._driver_dispatcher.schedule_pickup(order_id)
        self.shelves.store(order)
        # Procesar la order: inmediato
    
    def pickup_order(self, order_id: int):
        order = find_order_by_id(order_id)
        return self.shelves.pop_by_id(order_id)

    def shutdown(self):
        self.order_consumer.stop()