from datetime import datetime
from unittest.mock import MagicMock

from kitchen.kitchen import Kitchen
from kitchen.collector import WasteCollector
from kitchen.shelf_client.in_memory import InMemoryShelfClient
from kitchen.model import Shelf
from kitchen.model.order import OrderTemp, Order
from kitchen.shelf import OVERFLOW_SHELF, ShelfManager
from kitchen.dispatcher import DriverDispatcher
from kitchen.model.decay import DefaultDecayFormula


def test_first():
    # given
    shelf_client = InMemoryShelfClient()
    shelves = [
        Shelf(OrderTemp.COLD.value, 15),
        Shelf(OrderTemp.HOT.value, 15),
        Shelf(OrderTemp.FROZEN.value, 15),
        Shelf(OVERFLOW_SHELF, 20)
    ]
    waste_collector = WasteCollector(shelves, shelf_client, 1)
    dispatcher = DriverDispatcher()
    dispatcher.dispatch = MagicMock()
    shelf_manager = ShelfManager(shelf_client, shelves)
    kitchen = Kitchen(waste_collector, dispatcher, shelf_manager)
    # when
    decay_formula = DefaultDecayFormula(0.45)
    order = Order(name="burger",
                  temp=OrderTemp.HOT,
                  shelf_life=300,
                  decay=decay_formula,
                  creation_time=datetime.utcnow())
    result = kitchen.process_order(order)
    # then
    assert result is not None
