""" Get majority element in O(N) time
    and O(1) space
"""
def majority(arr):
    majority = 0
    count = 0
    for n in arr:
        print(n,count,majority)
        if count == 0:
            majority = n
        if n == majority:
            count+=1
        else:
            count-=1
    return majority


if __name__ == '__main__':
    #arr = [3,1,7,1,1,7,7,3,7,7,7]
    arr = [3,1,3,2,3,5,3,6,3,6,3]
    m = majority(arr)
    print(m)