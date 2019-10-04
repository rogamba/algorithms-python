""" Design an algorithm to to find the smallest 
    K numbers in an array

    Solution:
    - Iterate the array
    - Build a K length max heap

"""
import heapq

k = 3
arr = [5,3,2,8,4,5,7,2,1,4,6,9,8,6,0,-1,-4,100]

def eval_min(elem, heap):
    global k
    heap_elem = elem*-1
    if len(heap) < k:
        heapq.heappush(heap, heap_elem)
    else:
        max_heap = heap[0]
        if heap_elem > max_heap:
            heapq.heappop(heap)
            heapq.heappush(heap, heap_elem)

def min_k(arr):
    # Loop the array to valuate
    heap = []
    for a in arr:
        eval_min(a, heap)
    # Convert heap
    for i in range(len(heap)):
        heap[i]*=-1
    return heap

if __name__ == '__main__':
    kmin = min_k(arr)
    print("Get {} min elems of array: {}".format(
        k, arr
    ))
    print("Solution: ")
    print(kmin)
