""" Given two large trees,
    check if one tree is subtree
    of another tree
"""
from collections import deque

class Tree(object):

    def __init__(self, root=None):
        if root != None:
            root = self.Node(root)
        self.root = root

    class Node:
        def __init__(self, key):
            self.key=key
            self.right=None
            self.left=None

    def __str__(self):
        # Level traverse
        if not self.root:
            return " <empty tree> "
        s = ""
        queue = deque()
        queue.appendleft(self.root)
        queue.appendleft(None)
        while len(queue) > 0:
            current = queue.pop()
            if current == None:
                if len(queue) <= 0:
                    break
                s+="\n"
                queue.appendleft(None)
                continue
            s+="{} ".format(current.key)
            if current.left: queue.appendleft(current.left)
            if current.right: queue.appendleft(current.right)
        return s
            
    def add(self, k, parent=None):
        if self.root == None:
            self.root = self.Node(k)
            return
        if parent == None:
            parent = self.root
        # Add node where it should
        if k > parent.key:
            if not parent.right:
                parent.right = self.Node(k)
            else:
                self.add(k, parent.right)
        elif k < parent.key:
            if not parent.left:
                parent.left = self.Node(k)
            else:
                self.add(k, parent.left)
        else:
            raise ValueError("Cant have duplicate keys in a binary tree")
        return True


    def check_subtree(tree):
        # Traverse subtree
        # Traverse this tree
        # Compare strings



if __name__=="__main__":
    tree = Tree(10)
    tree.add(5)
    tree.add(3)
    tree.add(6)
    tree.add(7)
    tree.add(2)
    tree.add(15)
    tree.add(13)
    tree.add(18)
    print(tree)

