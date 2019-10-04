from datetime import timedelta, datetime


class DecayFormula(object):
    """Decay Formula interface.
    """
    def __init__(self, decay_rate: float = 0):
        self.decay_rate = decay_rate

    def compute(self, shelf_life: timedelta, creation_time: datetime) -> float:
        """[summary]
        
        :param shelf_life: [description]
        :type shelf_life: timedelta
        :param creation_time: [description]
        :type creation_time: datetime
        :return: [description]
        :rtype: float
        """
        raise NotImplementedError()


class DefaultDecayFormula(DecayFormula):
    """Default decay formula.
    """
    def compute(self, shelf_life: timedelta, creation_time: datetime) -> float:
        order_age = datetime.utcnow - creation_time
        return (shelf_life - order_age).total_seconds() - (
            self.decay_rate * order_age.total_seconds())
