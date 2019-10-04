""" Find the largest cluster of 1s in a
    matrix of 0s and 1s, it is consider a
    cluster if a 1 is in any adjacent position
    of another one (right, down, left, top).
    The method should receive a matrix and
    return the size of the cluster of 1s that
    are connected
"""
from collections import deque

# In the example the maximum
#  cluster of 1s is of size 4
board = [
    [0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 1]
]

def get_adjacent(row, col, cluster=False):
    global board
    adj = []
    if col < len(board[row])-1:
        adj.append((row, col+1))
    if row < len(board)-1:
        adj.append((row+1, col))
    if col > 0:
        adj.append((row, col-1))
    if row > 0:
        adj.append((row-1, col))
    
    return adj


def find_cluster(board, start=(0,0)):
    """ Solution:
        - BFS to traverse the board
        - DFS to get size of the cluster    
    """ 
    clusters=[]
    largest_cluster=0
    queue = deque([start])
    visited = []
    visited_cluster = []

    def traverse_cluster(cell, path=[]):
        nonlocal board, visited_cluster, clusters
        # Check if cell already visited in clusters
        if cell in visited_cluster:
            return
        if len(path) == 0:
            path.append(cell)
        # Base case there is no adjacent        
        visited_cluster.append(cell)
        adj_list = get_adjacent(*cell, cluster=True)
        # Remove adjacent not if 1s and already visited
        adj_list = [ (r,c) for r,c in adj_list if board[r][c] == 1 and (r,c) not in visited_cluster]
        # If no adjacent, append to clusters
        for adj_cell in adj_list:
            if adj_cell != None:
                row, col = adj_cell
                if adj_cell not in visited_cluster and board[row][col] == 1:
                    path.append(adj_cell)
                    traverse_cluster(adj_cell, path=path)

    # traverse the whole board
    while len(queue) > 0:
        row,col = queue.pop()
        # Check if visited in queue
        if (row, col) in visited:
            continue
        # Check if need to traverse cluster
        if board[row][col] == 1:
            path = []
            traverse_cluster((row, col), path=path)
            if len(path) > 0:
                clusters.append(path)
        # Visit and enqueue the adjacent 
        visited.append((row, col))
        adj_list = get_adjacent(row, col, cluster=False)
        for a in adj_list:
            queue.appendleft(a)
    
    return clusters

                
if __name__ == '__main__':
    from pprint import pprint
    clusters = find_cluster(board)
    print("Board layout:")
    for r in board:
        print(r)
    print()
    print("Clusters found: {} ")
    pprint(clusters)
    print()
    print("Size of all the clusters:")
    for cluster in clusters:
        print(len(cluster))