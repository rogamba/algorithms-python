""" A child runs up the stairs, he can give steps
    of 1, 2 or 3 steps at a time. Given the length of a
    stairs return the possible ways he can go up
"""
import time

class Node(object):
    def __init__(self, key, value=None):
        self.key = None
        self.value = None
        self.adj = []
    
class Stairs(object):
    def __init__(self, levels=10, max_step=1):
        self.levels = levels
        self.max_step = max_step
        self.nodes = {}
        self.build_graph()

    def add(self, f, t):
        if f not in self.nodes:
            self.nodes[f] = Node(f)
        if t not in self.nodes:
            self.nodes[t] = Node(t)
        if self.nodes[t] not in self.nodes[f].adj:
            self.nodes[f].adj.append(self.nodes[t])

    def build_graph(self):
        n = self.levels
        for i in range(n+1):
            for nxt in range(i+1, i+1+self.max_step):
                if nxt <= self.levels:
                    node = self.add(i, nxt)

    def find_paths(self):
        paths = []
        def _find_paths(node=None, path=[]):
            nonlocal paths
            if node == None:
                return
            if len(node.adj) == 0:
                paths.append(path)
            for adj in node.adj:
                _find_paths(node=adj, path=path[:]+[adj.key])
        _find_paths(node=self.nodes[0], path=[self.nodes[0].key])
        return paths


if __name__ == '__main__':
    start = time.time()
    stairs = Stairs(levels=20, max_step=3)
    paths = stairs.find_paths()
    end = time.time()
    print("All possible paths to climb up the stairs are: {}".format(len(paths)))
    print("Took {} ".format(end-start))