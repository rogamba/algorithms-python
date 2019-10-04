

# Everything with pointers
def quicksort(arr, s=0, e=None):
    if e == None:
        e = len(arr)-1
    # Base cases
    if s >= e:
        return
    # Pivot
    start, end = s, e
    p = s
    pivot = arr[p]
    # Reorder
    while s<=e:
        # Find the left unordered
        while arr[s] < pivot:
            s+=1
        # Find the right unordered
        while arr[e] > pivot:
            e-=1
        # Both fulfill condition
        if s <= e:
            #print(arr)
            tmp = arr[s]
            arr[s] = arr[e]
            arr[e] = tmp
            s+=1
            e-=1
    # Recurse
    quicksort(arr,start,s-1)
    quicksort(arr,s,end)

#arr = [6,3,9,8,5,2,7,1,15]
arr = [6,3,4,1,2]
quicksort(arr)
print(arr)