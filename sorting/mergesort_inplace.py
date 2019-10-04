def mergesort_pointers(arr, left=None, right=None):
    # Divide and conquer
    # Pointers
    left = left if left != None else 0
    right = right if right != None else len(arr)-1
    middle = int((right+left)/2)
    print("Left {} Middle {} Right {}".format(left, middle, right))
    # Base case
    if (right-left) <= 0:
        return

    # Recursive merge
    mergesort_pointers(arr,left,middle)
    mergesort_pointers(arr,middle+1,right)
    merge(arr,left,middle,right)

def merge(arr,l,m,r):
    # Sizes
    s1 = int(m-l)
    s2 = int(r-m)
    # Temporary arrays
    L = arr[l:m]
    R = arr[m:r]
    # pointers of arrays
    p1, p2 = 0, 0
    k = l
    print(L,R)
    # Loop and merge
    while p1 < s1 and p2 < s2:
        print(p1,p2)
        if L[p1] < R[p2]:
            arr[k] = L[p1]
            p1+=1
        else:
            arr[k] = R[p2]
            p2+=2
        k+=1
    
    # Remaining elements
    while p1 < s1:
        arr[k] = L[p1]
        p1+=1
        k+=1
    while p2 < s2:
        arr[k] = R[p2]
        p2+=1
        k+=1


if __name__=='__main__':
    # Do something...
    arr = [5,4,2,4,1,10]
    arr_sortred = mergesort_pointers(arr)
    print(arr)