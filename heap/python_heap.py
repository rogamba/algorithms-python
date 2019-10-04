""" Python implementation to use
    a heap with heapq
"""
import heapq

class Task(object):
    def __init__(self, rank=None):
        self.rank = rank

def run():
    # Heap of integers
    h = [42,29,18,14,7,18,12,11,13]
    heapq.heapify(h)
    heapq.heappush(h, 100)
    last = heapq.heappop(h)
    last = heapq.heappop(h)
    print(h)
    print(last)
    # Heap of objects
    print()
    print("Heap of objects")
    obs = [
        (10,Task(rank=10)),
        (5,Task(rank=5)),
        (90,Task(rank=90)),
        (3,Task(rank=3)),
    ]
    heapq.heapify(h)
    new_task = Task(rank=4)
    #heapq.heappush(h, (new_task.rank, new_task))
    print(obs)

if __name__ == '__main__':
    run()