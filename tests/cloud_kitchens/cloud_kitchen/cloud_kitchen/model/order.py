from datetime import datetime, timedelta
import time
import time
from enum import Enum
import uuid

class OrderTemp(Enum):
    HOT = "hot"
    COLD = "cold"
    FROZEN = "frozen"


class Order(object):
    """ Order represents a Kitchen Order coming into the system.
    """
    def __init__(
        self,
        id: int = None,
        name: str = "",
        temp: OrderTemp = None,
        shelf_life: timedelta = None,
        decay_rate: float = None,
        creation_time: float = None
    ):
        self.id = str(uuid.uuid4()) if not id else id
        self.name = name
        self.temp = temp
        self.shelf_life = shelf_life
        self.decay_rate = decay_rate
        self.creation_time = time.time() if not creation_time else creation_time

    def __str__(self):
        return "<Order id={} temp={} name={} shelf_life={} decay_rate={}>".format(
            self.id, self.temp, self.name, self.shelf_life, self.decay_rate
        )

    def normalized_value(self, decay_factor):
        return self.compute_value(decay_factor)/self.shelf_life 

    def is_waste(self, decay_factor) -> bool:
        """ Verify if order is already waste
        
        :return: Computed value of order's life
        :rtype: float
        """
        return self.compute_value(decay_factor) <= 0

    def compute_value(self, decay_factor) -> float:
        """ Verify if order is already waste
        
        :return: True or False depending if the order is waste or not
        :rtype: bool
        """
        order_age = time.time() - self.creation_time
        return (
            self.shelf_life - order_age
        ) - (
            self.decay_rate * decay_factor * order_age
        )
