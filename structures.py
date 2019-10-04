from collections import deque

# Dynamic Arrays
class DynamicArray(list):
    """ Characteristics:
        - Fast get, sets
        - Slow delete
    """

    def __init__(self, *args):
        self.capacity = len(args)
        for i in range(args):
            self.check_resize()
            self[i] = args[i]
        self.size = 0

    def get(self, idx):
        """ O(1) """ 
        return self[idx]

    def put(self, idx, value):
        """ O(1) """ 
        if idx > self.size:
            return False
        self[idx] = value

    def add(self, value):
        """ O(1) """ 
        i = self.size
        self.check_resize()
        self[i] = value
        self.size+=1
        pass

    def delete(self, idx):
        """ O(n) """ 
        # Copy down elements
        for i in range(idx, self.size):
            self[i] = self[i+1]
        # Resize
        self.size-=1

    def check_resize(self):
        # Check if should resize
        if self.size == self.capacity:
            self.resize()

    def resize(self):
        """ O(n) """ 
        # Initialize array
        tmp = self
        self = [ None for i in self.capacity*2 ]
        # Copy values 
        for i in range(self.capacity):
            self[i] = tmp[i]
        # Duplicate size
        self.capacity *= 2
        

# Linked List
class LinkedList(object):
    """ Properties:
        - Get head fast
        - Delete linear complexity
        - Super fast inserts
    """

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self, root=None):
        if root != None and type(root) == self.Node:
            self.root = root
            self.size = 1
        else:
            self.root = None
            self.size = 0

    def __str__(self):
        if self.root == None:
            return "Empty List"
        lst = ""
        node = self.root
        while node:
            lst += "{}".format(node.value)
            if node.next:
                lst+=" -> "
            node = node.next
        return lst

    def append(self, value):
        """ O(n) """ 
        new_node = self.Node(value)
        # If no root
        if self.root == None:
            self.root = new_node
            return
        # Find tail
        current_node = self.root
        while current_node.next:
            current_node = current_node.next
        # Assign tail
        current_node.next = new_node

    def prepend(self, value):
        """ O(1) """ 
        new_node = self.Node(value)
        new_node.next = self.root
        self.root = new_node

    def delete(self, value):
        """ O(n) """ 
        # Find and delete
        current = self.root
        while current.next != None:
            # Node to delete
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        return False


    def find(self, look):
        """ O(n) """ 
        current = self.root
        while current != None:
            if current.value == look:
                return True
            current = current.next
        return False
    
    def pop(self):
        """ O(1) """ 
        # Remove head
        if self.root == None:
            return None
        node = self.root
        self.root = node.next
        return node.value

    def get_size(self):
        """ O(1) """ 
        size = 0
        current = self.root
        while current != None:
            size+=1
            current = current.next
        return size

            
class HasTable(object):
    """ Properties
        - Super fast lookups: get, get -> O(1)
    """

    def __init__(self):
        self.size = 16
        # List of linked_lists
        for _ in range(self.size):
            self.data.append(None)

    def put(key, value):
        """ O(1) """ 
        idx = self.get_index(key)
        entry = self.Node(key, value)
        if self.data[idx] == None:
            self.data[idx] = LinkedList(root=entry)
        else:
            current = self.data[idx].root
            while current != None:
                current = current.next
            current.next=entry
            
    def get(self, key):
        """ O(1) """ 
        idx = get_index(key)
        if self.data[idx] == None:
            return None
        else:
            current = self.data[idx].root
            while current.next:
                if current.key == key:
                    return current.value
                current = current.next

    def get_index(self,  key):
        """ O(1) """ 
        # Hashing function
        return hash(key) % self.size


class Graph(object):
    """ Generalizations:
        - Nodes attribute as dict of nodes
        - Nodes have a list of adjancent
    """
    class Node:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
            self.adj = []
            self.visited = False
        def __str__(self):
            return "({}={})".format(self.key,self.value)
    
    def __init__(self):
        self.nodes = {}
        self.queue = deque()
        self.stack = deque()

    def __str__(self):
        rep = ""
        for k in self.nodes:
            adj = ""
            for a in self.nodes[k].adj:
                adj+=" {} ".format(a.__str__())
            rep+="{} => {}\n".format(k,adj)
        return rep
    
    def add(self, key_from, key_to):
        """ O(n) """ 
        # Check if node exists, if not add
        for k in [key_from, key_to]:
            if k not in self.nodes:
                self.add_node(k)
        # Check if key_to not in list of node from
        adj_node = self.nodes[key_to]
        if adj_node not in self.nodes[key_from].adj:
            self.nodes[key_from].adj.append(adj_node)

    def add_node(self, key):
        if key in self.nodes:
            return
        new_node = self.Node(key)
        self.nodes[key] = new_node

    def delete(self, key):
        # Remove all relationships
        if key not in self.nodes:
            return False
        # Remove the node from the adjacency list

    def bfs(self, start=None):
        if start not in self.nodes:
            print("root node doesn't exist")
            return
        # Implemented with stack
        self.queue.appendleft(start)
        while len(self.queue) > 0:
            k = self.queue.pop()
            print("Visiting {}".format(k))
            self.nodes[k].visited = True
            # Get nodes
            adj = self.nodes[k].adj
            for a in adj:
                if a.visited != True:
                    self.queue.appendleft(a.key)

    def dfs(self, start=None):
        if start not in self.nodes:
            print("root node doesn't exist")
            return
        # Implemented with stack
        self.stack.appendleft(start)
        while len(self.stack) > 0:
            k = self.stack.popleft()
            print("Visiting {}".format(k))
            self.nodes[k].visited = True
            # Get nodes
            adj = self.nodes[k].adj
            for a in adj:
                if a.visited != True:
                    self.stack.appendleft(a.key)
        
    def dfs_recursive(self, key=None):
        if key not in self.nodes:
            print("root node doesn't exist")
            return
        # Implemented recursively
        node = self.nodes[key]
        node.visited = True
        print("Visiting recursively {}".format(node.key))
        if len(node.adj) <= 0:
            return
        for a in node.adj:
            self.dfs_recursive(key=a.key)

    def reset_path(self):
        for k in self.nodes:
            self.nodes[k].visited = False



class MinGraph(object):
    
    class Node(object):
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            # List of adjacent node objects
            self.adj = []

    def __init__(self):
        # Adjacency list
        self.nodes = {}

    def add(self, f, t):
        if f not in nodes:
            self.nodes[f] = self.Node(key=f)
        if t not in nodes:
            self.nodes[t] = self.Node(key=t)
        if self.nodes[t] not in self.nodes[f].adj:
            self.nodes[f].adj.append(self.nodes[t])


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(4)
    ll.append(5)
    ll.append(1)
    ll.prepend(10)
    ll.delete(5)
    print(ll)

    print("Graph: ")
    graph = Graph()
    graph.add(0,1)
    graph.add(0,2)
    graph.add(0,3)
    graph.add(1,4)
    graph.add(1,5)
    graph.add(5,6)
    graph.add(5,7)
    graph.add(6,8)
    graph.add(3,9)
    graph.add(9,10)
    graph.add(10,11)
    print(graph)
    print("DFS:")
    graph.dfs(0)
    graph.reset_path()
    print("BFS:")
    graph.bfs(0)
    graph.reset_path()
    print("DFS recursive:")
    graph.dfs_recursive(key=0)



