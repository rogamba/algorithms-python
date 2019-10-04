import logging
import uuid

from .waste_collector import WasteCollector
from .dispatcher import Dispatcher
from .errors import DomainError
from .model.order import Order
from .order_queue import OrderQueue
from .shelf_manager import ShelfManager

LOG = logging.getLogger(__name__)


class CloudKitchen(object):
    """ Kitchen application instance
    
        :order_queue: OrderQueue
        :shelves: ShelfManager
        :dispatcher: Dispatcher
        collector: WasteCollector
    """
    def __init__(
        self, 
        order_queue: OrderQueue,
        shelves: ShelfManager,
        dispatcher: Dispatcher,
        collector: WasteCollector
    ):
        self.order_queue = order_queue
        self.order_queue.set_handler(self.process_order)
        self.order_queue.watch()
        self.dispatcher = dispatcher
        self.dispatcher.set_handler(self.pickup_order)
        self.dispatcher.start_dispatching()
        self.shelves = shelves
        self.collector = collector
        self.collector.start_collecting()

    def get_state(self):
        """ Get shelves state
        """
        return self.shelves.get_state()

    def process_order(self, order):
        """ Action to take whenever there's a new
            incomming order.
        
            :param order: [description]
            :type order: Order
            :return: [description]
            :rtype: str
        """
        if self._put_in_shelf(order):
            self._dispatch_order(order)
        return order

    def pickup_order(self, id: str) -> Order:
        """ Action to take when a driver picks up 
            an order.
        
            :param id: 
            :type id: str
            :return: 
            :rtype: Order
        """
        order = self.shelves.pop_by_id(id)
        if not order:
            self._record_metrics_invalid_order_pickup(id)
            return False
        return order

    def _put_in_shelf(self, order: Order) -> bool:
        """ Try to put order in it's corresponding
            shelf

            :order: Order
            :return: bool if we could place the order
        """
        try:
            if not self.shelves.put(order):
                LOG.warn(
                    "Unable to alocate order in any shelves, most likely all are full!"
                )
                return False
            return True
        except DomainError as e:
            LOG.exception(
                "Error while trying to put in shelf: order={}".format(order),
                e)
            return False

    def _dispatch_order(self, order: Order):
        """ Dispatch order through dispatcher client
            :order: Order object
        """
        self.dispatcher.dispatch(order)

    def _record_metrics_new_order(self, order: Order):
        LOG.info("Processed order: {}".format(order))

    def _record_metrics_invalid_order_pickup(self, id: str):
        LOG.warn("Invalid order id: {}".format(id))