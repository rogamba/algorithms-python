from collections import deque

class Graph(object):

    def __init__(self):
        self.nodes = {}
        self.queue = deque()
        self.add_node(0)

    def __str__(self):
        s = ""
        for k in self.nodes:
            s+="{} => {}".format(
                k,
                [ a.key for a in self.nodes[k].adj ]
            )
            s+="\n"
        return s

    class Node:
        def __init__(self, key):
            self.key = key
            self.adj = []
    
    def add(self, f, t):
        if f not in nodes:
            self.nodes[f] = Node(key=f)
        if t not in nodes:
            self.nodes[t] = Node(key=t)
        # Check if it's adjacent
        if self.nodes[t] not in self.nodes[f].adj:
            self.nodes[f].adj.append(self.nodes[t])

    def visit(self, node):
        if not hasattr(node, "key"):
            return False
        print("Visiting {} ".format(node.key))
    
    def bfs(self, start=0 ):
        visited = set()
        current = self.nodes[start]
        self.queue.appendleft(current)
        visited.add(current.key)
        # Loop
        while len(self.queue) > 0:
            current = self.queue.pop()
            self.visit(current)
            # Adjacent
            if current.adj:
                for n in current.adj:
                    if n.key not in visited:
                        self.queue.appendleft(n)
                        visited.add(n.key)

    def dfs(self, start=0):
        visited = set()
        # Recursive search for adjacent nodes
        def _dfs(key):
            node = self.nodes[key]
            self.visit(node)
            visited.add(node.key)
            if node.adj:
                for n in node.adj:
                    if n.key not in visited:
                        _dfs(n.key)
        
        _dfs(start)
        return


if __name__ == '__main__':
    graph = Graph()
    graph.add(0,1)
    graph.add(0,2)
    graph.add(0,3)
    graph.add(1,2)
    graph.add(1,4)
    graph.add(1,5)
    print(graph)
    print("Breath First Search")
    graph.bfs()
    print()
    print("Depth First Search")
    graph.dfs()

                

                
