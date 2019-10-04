
arr = [5,6,3,4,6,8,3,2,1,1,3,5]

def quicksort(arr):
    if len(arr) <= 0:
        return []
    if len(arr) == 1:
        return arr
    pivot = arr[-1]
    # Exclude
    left = [i for i in arr if i<pivot]
    equal = [e for e in arr if e==pivot]
    right = [r for r in arr if r>pivot]
    return quicksort(left) + equal + quicksort(right)