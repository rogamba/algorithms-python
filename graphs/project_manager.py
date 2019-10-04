""" Given a list of projects and dependencies on the projects
    themselves, find a build order that will allow the projects to be built. 
    If there is no valid build order, return an error
    Projects: a, b, c, d, e, f
    Dependencies: (a,d), (f,b), (b,d), (f, a), (d,c)
    Output: f, e, a, b, d, c
"""
import copy
from collections import deque

class ProjectManager(object):

    class NodeList(list):
        def __init__(self):
            pass
        def __str__(self):
            rep = ""
            for x in self.__iter__():
                rep+=" {} ".format(x.key)
            return "[{}]".format(rep)

    class Node:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
            self.next = ProjectManager.NodeList()
            self.required = ProjectManager.NodeList()
        def __str__(self):
            return "Node({})".format(self.key)

    def __init__(self):
        # Adjacency list
        self.nodes = {}

    def __str__(self):
        rep = ""
        for k, v in self.nodes.items():
            rep+="({}) ==>  {}".format(k, v.next)
            rep+="\n"
        return rep

    def add(self, key_from, key_to):
        self.add_edge(key_from, key_to)

    def add_node(self, key):
        if key in self.nodes:
            return
        new_node = self.Node(key)
        self.nodes[key] = new_node
        return self

    def add_edge(self, key_from, key_to):
        if key_from not in self.nodes:
            self.add_node(key_from)
        if key_to not in self.nodes:
            self.add_node(key_to)

        node_from = self.nodes[key_from]
        node_to = self.nodes[key_to]

        if node_to not in node_from.next:
            node_from.next.append(node_to)
            node_to.required.append(node_from)

        return self
        
    def create_graph(self, nodes, dependencies):
        """ Given list of dependencies, create
            the graph
        """
        for n in nodes:
            self.add_node(n)
        for d in dependencies:
            self.add(d[0],d[1])


    def get_leaves(self):
        leaves = []
        for k in self.nodes:
            if len(self.nodes[k].next) <= 0:
                leaves.append(self.nodes[k])
        return leaves


    def get_roots(self, nodes=None):
        roots = self.NodeList()
        for k in self.nodes:
            if len(self.nodes[k].required) == 0:
                roots.append(self.nodes[k])
        return roots


    def get_order(self):
        roots = self.get_roots()
        queue = deque()
        for root in roots:
            queue.appendleft(root)
        # All nodes to get them visited
        queued = {}
        for key in self.nodes:
            queued[key] = False
        # Visit nodes
        order = []
        while len(queue) > 0:
            current = queue.pop()
            order.append(current.key)
            for nxt in current.next:
                if not queued[nxt.key]:
                    queue.appendleft(nxt)
                    queued[nxt.key] = True
        return order

        

if __name__=='__main__':
    pm = ProjectManager()
    projects = ['a','b','c','d','e','f','h']
    dependencies = [
        ('a','d'),
        ('f','b'),
        ('b','d'),
        ('f','a'),
        ('d','c'),
        ('e','h')
    ]
    pm.create_graph(projects,dependencies)
    print(pm)

    # Recommended order
    order = pm.get_order()
    print(order)
    print()
