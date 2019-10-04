""" Create a class that can iterate
    the elements of an array of arrays like:

    [[],[1,2,3],[],[4,5],[6],[],[],[7,8,9]]

    Methods to implement:
    __init__
    has_next - check if has next element
    next - get the next element of the subarrays
    remove - remove the last element returned by next

"""


class Iterator(object):

    def __init__(self, data=None):
        self.data = data
        self._p = 0
        self._psub = 0
        self.set_pointers()
        self.last_value = (None, None)
    
    def __str__(self):
        return str(self.data)

    def set_pointers(self):
        if self._psub < len(self.data[self._p])-1:
            self._psub+=1
        elif self._p < len(self.data)-1:
            self._psub=0
            self._p+=1
            while not self.data[self._p]:
                self._p+=1
        # Eval if we reached the end
        elif self._p == len(self.data)-1 and self._psub == len(self.data[self._p])-1:
            self._p = -1
            self._psub = -1

    def has_next(self):
        # Check if data has elements
        if not self.data:
            return False
        # Check element of the pointer
        if self._p != -1 and self._psub != -1:
            return True

    def next(self):
        # Get next element of the subarrays
        if self._p == -1:
            return False
        # Value to return
        value = self.data[self._p][self._psub]
        self.last_value = self._p, self._psub
        # Increment pointers to the next value
        self.set_pointers()
        return value

    def remove(self):
        # Copy list without the element
        p, psub = self.last_value
        if p == None or psub == None:
            return False
        # Copy without the element
        tmp = self.data[p]
        self.data[p] = tmp[:psub]
        if self._psub < len(tmp):
            self.data[p] += tmp[psub+1:]


if __name__ == '__main__':
    arr = [[],[1,2,3],[],[4,5],[6],[],[],[7,8,9]]
    it = Iterator(arr) 
    while it.has_next():
        print(it.next())
    print(it)
    it.remove()
    print(it)
    #print(it.has_next())
    #print(it.next())
    #print(it.next())
    #print(it.next())
    #print(it.next())
    #print(it.next())
    #print(it.next())
    #print(it.next())
    #print(it.next())
    


        
        
        

    
