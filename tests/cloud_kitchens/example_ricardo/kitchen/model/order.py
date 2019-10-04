from datetime import datetime, timedelta
from enum import Enum

from .decay import DecayFormula


class OrderTemp(Enum):
    HOT = "hot"
    COLD = "cold"
    FROZEN = "frozen"


class Order(object):
    """
    Order represents a Kitchen Order coming into the system.
    """
    def __init__(self,
                 id: int = None,
                 name: str = "",
                 temp: OrderTemp = None,
                 shelf_life: timedelta = None,
                 decay: DecayFormula = None,
                 creation_time: datetime = None):
        self.id = id
        self.name = name
        self.temp = temp
        self.shelf_life = shelf_life
        self.decay = decay
        self.creation_time = creation_time

    def is_waste(self) -> bool:
        """[summary]
        
        :return: [description]
        :rtype: bool
        """
        return self.decay.compute(self.shelf_life, self.creation_time) <= 0
