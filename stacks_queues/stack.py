class Stack(object):
    class Node:
        def __init__(self, data, minimum=None):
            self.data = data
            self.min = minimum
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        rep = ""
        if not self.head:
            return "[]"
        # Iterate to tail
        current = self.head
        while current != None:
            rep += " {} ".format(current.data)
            if current.next:
                rep+=" -> "
            current = current.next
        return "[{}]".format(rep)


    def push(self, data):
        _min = data
        if self.head != None:
            _min = self.min()
        new_node = self.Node(data, min(data,_min))
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        

    def pop(self):
        if self.head == None:
            raise Exception("Empty head!")
        data = self.head.data
        self.head = self.head.next
        return data

    def min(self):
        return self.head.min

if __name__ == '__main__':
    """ Implement a O(1) access to the
        minimum element of the stack
    """
    stack = Stack()
    stack.push(10)
    stack.push(4)
    stack.push(3)
    stack.push(5)
    stack.push(1)
    print("Stack: ")
    print(stack)
    print()


    stack.pop()
    print("Minimum of:")
    print(stack)
    print(stack.min())