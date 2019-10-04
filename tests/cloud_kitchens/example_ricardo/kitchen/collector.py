from threading import Thread
import logging
import time

from .shelf import ShelfClient

LOG = logging.getLogger(__name__)


class WasteCollector(object):
    """[summary]
    """
    def __init__(self, shelves: list, shelve_client: ShelfClient,
                 poll_frequency: int):
        self.shelves = shelves
        self.client = shelve_client
        self.thread = Thread(target=self._cleanup)

    def start_collecting(self):
        """[summary]
        """
        if self.thread.isAlive():
            return
        self.thread.start()

    def _cleanup(self):
        while True:
            for shelf in self.shelves:
                for order in self.client.iterate_all_orders(shelf.name):
                    if (order.is_waste()):
                        order = self.client.pop_by_id(order.id)
                        LOG.info("Order {} was marked as waste and collected".
                                 format(order.id))
            time.sleep(self.poll_frequency)
