class LinkedList(object):

    class Node:
        def __init__(self, key):
            self.key = key
            self.next = None

    def __init__(self):
        self.head = None

    def __str__(self):
        rep = ""
        if not self.head:
            return "[]"
        # Iterate to tail
        current = self.head
        while current != None:
            rep += " {} ".format(current.key)
            if current.next:
                rep+=" -> "
            current = current.next
        return "[{}]".format(rep)

    def prepend(self, key):
        """ Add at the begginging of the list
        """
        new_node = self.Node(key)
        if not self.head:
            self.head = new_node
            return
        # Append
        tmp_node = self.head
        new_node.next = tmp_node
        self.head = new_node
        return self

    def append(self, key):
        """ Add at the tail of the list
        """
        new_node = self.Node(key)
        if not self.head:
            self.head = new_node
            return
        # Iterate to tail
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def pop(self):
        """ Pop head element from the list
        """
        if not self.head:
            return None
        result_node = self.head
        if result_node.next:
            head_to_be = result_node.next
            self.head = head_to_be
        else:
            self.head = None
        return result_node.key
        


    def delete(self, target):
        """ Erase node adjusting the pointers
        """
        current = self.head
        # case it's the head
        if current.key == target:
            self.head = self.head.next
        while current != None:
            if current.next:
                if current.next.key == target:
                    current.next = current.next.next
            current = current.next
                
    
    def find(self, target):
        """ Start with the head and iterate
        """
        current = self.head
        while current != None:
            if current.key == target:
                return True
            current = current.next
        return False

    def has_loop(self):
        """ With fast and slow nodes
        """
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print("Starting with the list:")
    print(ll)
    print()

    n = 3
    print("Finding {} in the Linked List?".format(n))
    print(ll.find(n))
    print()

    elem = ll.pop()
    print("Popped the head ({}) of the list".format(elem))
    print(ll)
    print()

    ll.prepend(100)
    print("Prepended element in the list:")
    print(ll)
    print()

    ll.delete(3)
    print("Deleted 3 from the list:")
    print(ll)
    print()

    print("Loop detection, adding loop:")
    ll.head.next.next.next = ll.head
    print(ll.has_loop())