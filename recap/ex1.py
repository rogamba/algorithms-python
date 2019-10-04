''' Iterator class 
    [[],[1,2,3],[],[4,5],[6],[],[],[7,8,9]]
'''


class Iterator(object):
    def __init__(self, data=[]):
        self.data = data
        self.prev = None
        self.p = 0
        self.ps = 0
        self.set_next_pointer()

    def __str__(self):
        return str(self.data)

    def set_next_pointer(self):
        p=self.p
        ps=self.ps+1
        while p < len(self.data):
            while ps < len(self.data[p]):
                if self.data[p][ps]:
                    self.p = p
                    self.ps = ps
                    return True
                ps+=1
            # Increment
            ps=0
            p+=1
        self.p = None
        self.ps = None
        return False

    def has_next(self):
        if self.p != None and self.ps != None:
            return True
        else:
            return False
    
    def next(self):
        # Check if there's next pointer
        value = self.data[self.p][self.ps]
        self.prev = (self.p, self.ps)
        self.set_next_pointer()
        return value

    def remove(self):
        """ Remove the last pointed element
        """
        if not self.prev:
            return False
        else:
            p, ps = self.prev
            self.data[p].pop(ps)
            self.p = p 
            self.ps = ps
            self.set_next_pointer()
        


if __name__=='__main__':
    arr = [[],[1,2,3],[],[4,5],[6],[],[],[7,8,9]]
    it = Iterator(arr)
    #while it.has_next():
    #    print(it.next())
    print(it)
    print(it.next())
    print(it.next())
    print(it.next())
    it.remove()
    print(it)
    print(it.next())
    print(it.next())
    it.remove()
    print(it)
    print(it.next())
    print(it.next())
