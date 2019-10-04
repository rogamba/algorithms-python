""" Given a stair of n steps,
    develop a method to find all 
    possible combinations to get to the
    top, if you can give steps of maximum
    3 steps

    Representation:

                    0
        1           2           3
    2   3  4     5  6  7     8  9  10

    Steps: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

"""
from pprint import pprint
import time


def find_paths(n, step_size):
    stairs = { i for i in range(n+1)}
    paths = []

    def move_step(stairs, step=0, path=[]):
        # Adjacent indexes
        nonlocal paths, step_size
        adj = []
        for nxt in range(step+1,step+1+step_size):
            if nxt in stairs:
                adj.append(nxt)
        # We reached the end of the stair
        if not adj:
            paths.append(path)
        # Recursion
        for node in adj:
            move_step(stairs, step=node, path=path[:]+[node])

    move_step(stairs, step=0, path=[0])
    return paths


if __name__ == '__main__':
    steps = 20
    step_size = 3
    start = time.time()
    paths = find_paths(steps, step_size)
    print("All paths for climbing up the stairs: {}".format(len(paths)))
    end = time.time()

    print("Took {} ".format(end-start))

    #pprint(paths)