import logging
import uuid

from .collector import WasteCollector
from .dispatcher import DriverDispatcher
from .errors import DomainError
from .helpers.validation import OrderValidator
from .model.order import Order
from .shelf import ShelfManager

LOG = logging.getLogger(__name__)


class Kitchen(object):
    """[summary]
    """
    def __init__(self, collector: WasteCollector, dispatcher: DriverDispatcher,
                 shelves: ShelfManager):
        self.collector = collector
        self.dispatcher = dispatcher
        self.shelves = shelves
        self.collector.start_collecting()

    def process_order(self, order: Order) -> str:
        """[summary]
        
        :param order: [description]
        :type order: Order
        :return: [description]
        :rtype: str
        """
        OrderValidator.validate(order)
        order.id = self._generate_order_id()
        if self._put_in_shelf(order):
            self._dispatch_order(order)
        self._record_metrics_new_order(order)
        return order.id

    def _generate_order_id(self):
        return str(uuid.uuid4())

    def _put_in_shelf(self, order: Order) -> bool:
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
        self.dispatcher.dispatch(order)

    def pickup_order(self, id: str) -> Order:
        """[summary]
        
        :param id: [description]
        :type id: str
        :return: [description]
        :rtype: Order
        """
        order = self.shelves.pop_by_id(id)
        if not order:
            return None
            self._record_metrics_invalid_order_pickup(id)
        return order

    def _record_metrics_new_order(self, order: Order):
        LOG.info("Processed order: {}".format(order))

    def _record_metrics_invalid_order_pickup(self, id: str):
        LOG.warn("Invalid order id: {}".format(id))
