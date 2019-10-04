""" Create a binary search tree class
    
"""
from collections import deque

class BinaryTree(object):

    class Node:
        def __init__(self, key):
            self.key = key
            self.right = None
            self.left = None
        def __str__(self):
            rep = ""
            rep+=" {} ".format(self.key)
            return "Node({})".format(self.key)


    def __init__(self):
        self.root = None
        self.queue = deque()


    def __str__(self, node=None):
        """ Printing level traversal
        """
        if self.root == None:
            return
        # Root node
        if node==None:
            node = self.root
        self.queue.appendleft(node)
        self.queue.appendleft(None)
        # While
        rep = ""
        while len(self.queue) > 0:
            node = self.queue.pop()
            if node != None:
                rep+=" {} ".format(node.key)
                if node.left:
                    self.queue.appendleft(node.left)
                if node.right:
                    self.queue.appendleft(node.right)
            else:
                rep+="\n"
                if len(self.queue) >= 1:
                    self.queue.appendleft(None)
        return rep
        
        
    def bfs(self):
        """ Breath-First Search implementation
            with a queue
        """
        # Empty queue
        if len(self.queue) > 0:
            self.queue.clear()
        # Start form the root
        self.queue.appendleft(self.root)
        while len(self.queue) > 0:
            node = self.queue.pop()
            print("Visiting node {}".format(node.key))
            if node.left:
                self.queue.appendleft(node.left)
            if node.right:
                self.queue.appendleft(node.right)


    def dfs(self, node=None):
        """ Depth-First Search implementation
            with recursion
        """ 
        if node == None:
            node = self.root
        if not node:
            raise Exception("No root node assigned")
        print("Visiting node {}".format(node.key))
        node.visited = True
        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)


    def insert(self, key, current=None):
        # Adding root node
        node = self.Node(key)
        if self.root == None:
            self.root = node
            return
        # First node
        if current == None:
            current = self.root
        # Append to the right
        if node.key > current.key:
            if current.right:
                self.insert(node.key, current.right)
            else:
                current.right = node
                return
        else:
            if current.left:
                self.insert(node.key, current.left)
            else:
                current.left = node
                return


if __name__ == '__main__':

    # Create the tree
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(6)
    tree.insert(2)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    tree.insert(12)
    tree.insert(16)

    # Printing the tree
    print()
    print("Printing level traversal of tree")
    print(tree)