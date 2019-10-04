""" Quick sort is one of the best algorithms for sorting
    elements in a list. It takes a pivot, say the first element
    of the list, and compares all other elements with the pivot.
    all the elements less than the pivot should be in the first
    part and the greater in the second part of the list. 
    This is done recursively.
"""

class SuperList(list):

    def __init__(self, *args):
        for a in args:
            self.append(a)

    def quick_sort(self, arr=None):
        sorted_arr = self._quick_sort()
        self.clear()
        for a in sorted_arr:
            self.append(a)

    def _quick_sort(self, arr=None):
        if arr==None:
            arr = self
        # base case
        if arr == []:
            return arr
        else:
            pivot = arr[0]
            lesser = [ a for a in arr if a < pivot ]
            equal = [ a for a in arr if a == pivot ]
            greater = [ a for a in arr if a > pivot ]
            return self._quick_sort(lesser) + equal + self._quick_sort(greater)


    def quicksort_pointers(self, left=None, right=None):
        # Check all the elems less than the pivot
        l = left if left != None else 0
        r = right if right != None else len(self)-1
        p = int((r+l)/2)
        # Base case
        if (r-l) == 0:
            return 
        
        # Init indexes
        init_l = l
        init_r = r
        init_p = self[p]

        while l <= r:
            # Move until the element is greater than the pivot
            while self[l] < init_p and l <= init_r:
                l+=1
            # Move until the element is smaller than the pivot
            while self[r] > init_p and r >= init_l:
                r-=1
            # Swap
            if l <= r:
                tmp = self[l]
                self[l] = self[r]
                self[r] = tmp
                l+=1
                r-=1   

        index = l
        quicksort_pointers(self, init_l, index-1)
        quicksort_pointers(self, index, init_r)



if __name__ == '__main__':
    test = SuperList(4, 7, 14, 1, 3, 9, 17)
    print("Initial List:")
    print(test)
    test.quick_sort()
    print("After Quick Sort:")
    print(test)