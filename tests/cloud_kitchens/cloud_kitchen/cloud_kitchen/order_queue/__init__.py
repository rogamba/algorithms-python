from abc import ABCMeta
from collections import deque

class OrderQueue(metaclass=ABCMeta):
    """ Abstract class for consuming incomming 
        orders
    """
    def set_handler(self):
        """ Set handler function to process the incomming
            orders
        """
        raise NotImplementedError()
        
    def watch(self):
        """ Start watching incomming orders
        """
        raise NotImplementedError()

