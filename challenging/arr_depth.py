""" Given an array of either integers or arrays, 
    get the sum of the products of each element
    of the array times the depth, where depth
    is largest at the topest level
"""
# [1, [1], 1] = 5
# [1, [1, [1] ], 1] = 1*3 + (1*2 + 1*1) + 1*3 = 9

from collections import deque

def nested_sum(arr):
    # Add first element to the queue
    queue = deque([(a, 1) for a in arr])
    items = []
    max_depth = 1
    while len(queue) > 0:
        elem, d = queue.pop()
        if type(elem) == list:
            for e in elem:
                queue.appendleft( (e, d+1 ) )
        else:
            items.append( (elem, d) )
            if d > max_depth:
                max_depth = d
    
    total = 0
    print(items)
    for i in range(len(items)):
        v, d = items[i]
        depth_value = max_depth+1-d
        print(v, depth_value)
        total+=(v*depth_value)

    return total



def nested_sum_rec(arr):

    items = []
    max_depth = 1
    def _nested_sum_rec(arr, d=1):
        # Base case
        nonlocal max_depth
        if type(arr) == int:
            if d > max_depth:
                max_depth = d
            items.append( (arr, d) )
        else:
            for a in arr:
                _nested_sum_rec(a, d=d+1)
        return

    _nested_sum_rec(arr)
    # reverse depth
    total = 0
    print(items)
    for v, d in items:
        dv = (max_depth-d+1)
        print(v, dv)
        total+=(v*dv)
    
    return total


if __name__=='__main__':
    test = [1, [1, [1] ], 1]
    print("Testing {} with recursion".format(test))
    s = nested_sum_rec(test)
    print("Result: {}".format(s))
    print()
    print("Testing {} with queue".format(test))
    s2 = nested_sum(test)
    print("Result: {}".format(s2))