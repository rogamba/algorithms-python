class Shelf(object):
    """ Shelf parent class
    """
    def __init__(self, name: str, capacity: int, decay_factor: int=1):
        self.name = name
        self.capacity = capacity
        self.decay_factor = decay_factor
