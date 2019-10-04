class Queue(object):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = self.Node(data)
        if self.tail != None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head == None:
            self.head = self.tail

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return data