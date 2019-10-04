from abc import ABCMeta

class Broker(metaclass=ABCMeta):
    """ Abstract class that simulates the order
        placement by clients
    """
    def stamp_rate(self):
        """ Stamp order elements with placement time
            :rate
        """
        raise NotImplementedError()

    def start_placing(self):
        """ Start simulation loop of order
            placement
        """
        raise NotImplementedError()

