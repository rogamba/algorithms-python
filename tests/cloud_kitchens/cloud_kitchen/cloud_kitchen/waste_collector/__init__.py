from threading import Thread, Lock
import logging
import time

from ..model.shelf import Shelf
from ..shelf_client import ShelfClient

LOG = logging.getLogger(__name__)


class WasteCollector(object):
    """ Waste collector class, executed in separate 
        thread and monitors kitchen shelves to clean
        them if there are orders gone to waste
        :shelves: list of dictionaries
        :shelf_client: injected shelf client dependency
    """
    def __init__(
        self, 
        shelves: [],
        shelf_client: ShelfClient,
        poll_frequency: int
    ):
        self.client = shelf_client
        self.shelves = {}
        for shelf in shelves:
            self.shelves[shelf['name']] = shelf
        self.poll_frequency = poll_frequency
        self.thread = Thread(target=self._cleanup)
        self.waste = []

    def start_collecting(self):
        """[summary]
        """
        if self.thread.isAlive():
            return
        self.thread.start()

    def _cleanup(self):
        while True:
            time.sleep(self.poll_frequency)
            lock = Lock()
            with lock:
                for name in self.client.shelves:
                    for order in self.client.iterate_all_orders(name):
                        if (order.is_waste(decay_factor=self.shelves[name]['decay_factor'])):
                            order = self.client.pop_by_id(order.id)
                            LOG.info("Order {} was marked as waste and collected".
                                    format(order.id))
