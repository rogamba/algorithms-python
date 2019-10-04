""" Merge sort is based in the divide and conquer
    approach, it first divides the initial array into
    sub arrays recursively until they're 2 elements arrays.
    Then the merge is applied comparing every element of each array 
    and putting the smaller in the next position and so on.
"""

class SuperList(list):

    def __init__(self, *args):
        for a in args:
            self.append(a)

    def merge_sort(self, l=None, r=None):
        # Initial pointers
        if l == None:
            l = 0
        if r == None:
            r = len(self)-1
        
        if l < r:
            print("Merging sort... arr[{}..{}]".format(l,r))
            # Middle point
            m = int((l+r)/2)
            # Sort halves
            self.merge_sort(l, m)
            #print("Passing to other side... arr[{}..{}]".format(m+1,r))
            self.merge_sort(m+1, r)
            # Merge
            #print("Merging... [{}..{}..{}]".format(l,m,r))
            self.merge(l,m,r)
            

    def merge(self, l, m, r):
        """ Merges two subarrays
            - first is l - m
            - second is m+1 - r
        """
        print("Merging {} {} {}".format(l,m,r))
        n1 = m-l+1
        n2 = r-m
        print(n1, n2)
        # Temp arrays
        L = [ self[l+i] for i in range(0,n1) ]
        R = [ self[m+1+j] for j in range(0,n2) ]
        print(L,R)
        # While pointer
        i,j = 0,0
        k = l
        while (i < n1 and j < n2):
            if L[i] <= R[j]:
                self[k] = L[i]
                i+=1
            else:
                self[k] = R[j]
                j+=1
            k+=1

        # Copy remaining elements of L
        while i < n1:
            self[k] = L[i]
            i+=1
            k+=1
        while j < n2:
            self[k] = R[j]
            j+=1
            k+=1
        #print("After merge... {}".format(self))
        #print()


if __name__ == '__main__':
    test = SuperList(38,27,43,3)
    print("Initial List:")
    print(test)
    test.merge_sort()
    print("After Merge Sort:")
    print(test)