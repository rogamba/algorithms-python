from . import Broker
from ..errors import DomainError
from collections import deque
from threading import Thread, Lock
import json
import math
import random
import time
import sys

class FileBasedBroker(Broker):
    """ Implementation of broker taking simulated
        orders from a file
    """
    def __init__(self, filename: str="", queue: deque=None, incomming_rate: int=1):
        """ Read the orders from a file
        """
        # Load data form file
        self.load_data(filename)
        # Average order rate, 1 ops by default
        self.incomming_rate = 1 if not incomming_rate else incomming_rate
        self.queue = queue
        self.calculate_rate()
        self.stamp_orders()
        self.thread = Thread(target=self._simulate)


    def start_placing(self):
        """ Check if thread is alive and start execution
        """
        if self.thread.isAlive():
            return
        self.thread.start()

        
    def load_data(self, filename: str):
        """ Load orders from file
            :filename: str name of the file inside /data dir
        """
        print('data/{}'.format(filename))
        if ".json" not in filename:
            raise DomainError("Only JSON file type accepted")
        with open('data/{}'.format(filename)) as file:
            self.orders = deque(json.load(file))
            


    def calculate_rate(self):
        """ Propability of event occurring every 1 miliseconds
        """
        # Total time 
        self._period = len(self.orders)*(1/self.incomming_rate)
        # Frecuency of the infinite loop 1ms
        self._tau = 0.001 
        self._lambda = self.incomming_rate * self._tau
        # Probability of occurrency every 1ms
        self._probability = ((self._lambda**1)*math.exp(-1*self._lambda))/math.factorial(1)


    def stamp_orders(self):
        """ Calculate placement time for every 
            order and add the timestamp in ms to each element
        """
        initial_time = int(time.time()*1000)
        delta = 0
        idx = 0
        while idx < len(self.orders):
            # Order placed
            if random.random() <= self._probability:
                self.orders[idx]['placement_stamp'] = delta
                idx+=1
            # Calculate
            delta+=1
        self.orders_stamped = True


    def _simulate(self):
        """ Start simulation of new
            order placements based on their
            timestamps
        """
        if not self.orders_stamped:
            raise Exception("Can't execute simulation without stamping orders first")
        # Loop all orders
        initial_time = int(time.time()*1000)
        current_order = None
        while len(self.orders) > 0:
            now = int(time.time()*1000)
            if not current_order:
                current_order = self.orders.popleft()
                order_stamp = initial_time+current_order['placement_stamp']
                continue
            # Compare now vs timestamp
            if now > order_stamp:
                self.place_new_order(current_order)
                current_order = None
        # Exit process
        sys.exit()


    def place_new_order(self, order):
        """ Place order to the kichen's queue 
            without the placement stamp
        """
        new_order = { k:v for k,v in order.items() if k != 'placement_stamp'}
        lock = Lock()
        with lock:
            self.queue.appendleft(order)
        return True
