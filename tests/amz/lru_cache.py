""" Build a cache class that applies the LRU
    eviction policy (Least Recently Used)
"""

class Node:
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data 
        self.next = None
        self.prev = None
        self.size = 0

class Cache(object):
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.images = {}
        self.capacity = capacity

    def __str__(self):
        s=[]
        if not self.head:
            return "<empty cache>"
        current = self.head
        while current:
            s.append(str(current.key))
            current = current.next
        return " -> ".join(s)
        
    def get(self, img_id):
        # Get and reorder
        if img_id not in self.images:
            return False
        # Reorder
        img_node = self.images[img_id]
        # Refresh cache
        self.refresh(img_node)
        return img_node
    
    def put(self, img_id, img):
        # Check if already exists
        if img_id not in self.images:
            self.images[img_id] = Node(key=img_id, data=img)
        # Get node from map
        img_node = self.images[img_id]
        # Reorder
        self.refresh(img_node)

    def refresh(self, node):
        # Pop the least recently used 
        if self.head == None:
            self.head = node
        if self.tail == None:
            self.tail = node
        # We've accessed the most recently used
        if self.head == node:
            return
        # Modify connections
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        # Check if tail
        self.check_tail(node)
        # Set head
        self.check_head(node)
        # Check if capacity has been reached
        if len(self.images) > self.capacity:
            print("Evicted")
            evicted_id = self.tail.key
            new_tail = self.tail.prev
            self.tail.prev.next = None
            del self.images[evicted_id]
            self.tail = new_tail

    def check_tail(self,node):
        # Update tail
        if self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None

    def check_head(self, node):
        curr_head = self.head
        curr_head.prev =  node
        self.head = node
        self.head.prev = None
        self.head.next = curr_head
            

if __name__ == '__main__':
    cache = Cache(5)
    cache.put(1,"hola")
    cache.put(2,"como")
    cache.put(3,"estas")
    cache.put(4,"esta")
    cache.get(1)
    print(cache)
    cache.put(5,"es")
    print(cache)
    #print(cache)
    cache.put(6,"una")
    print(cache)
    #print(cache)
    cache.put(7,"prueba")
    cache.put(8,"prueba1")
    cache.put(9,"prueba2")
    cache.put(10,"prueba3")
    print(cache)