from threading import Lock, Thread
import json
from collections import deque
import random
import time
import math

class Broker(object):
    """ Class that simulates the order
        placement at a given rate 
    """

    def __init__(self, queue=None, avg_rate=None):
        # read the file and store orders in memory
        try:
            with open('data/orders.json') as file:
                self.orders = deque(json.load(file))
        except FileNotFoundError as e:
            logger.error("[Broker] Could not locate orders file ")
        # Average order rate, 1 ops by default
        self.avg_rate = 1 if not avg_rate else avg_rate
        self.queue = deque() if not queue else queue
        self.calculate_rate()
        self.stamp_orders()
        self.lock = Lock()
        

    def calculate_rate(self):
        """ Propability of event occurring every 1 miliseconds
        """
        # Total time 
        self._period = len(self.orders)*(1/self.avg_rate)
        # Frecuency of the infinite loop 1ms
        self._tau = 0.001 
        self._lambda = self.avg_rate * self._tau
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


    def simulate_placement(self):
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
        return


    def place_new_order(self, order):
        """ Place order to the kichen's queue 
            without the placement stamp
        """
        new_order = { k:v for k,v in order.items() if k != 'placement_stamp'}
        self.lock.acquire()
        self.queue.appendleft(order)
        print(new_order)
        self.lock.release()
        return True
