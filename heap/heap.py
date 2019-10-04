""" Binary Heap:
        
                42
              /     \ 
            29       18
           /  \     /   \ 
          14   7   18   12
        [42,29,18,14,7,18,12]    

"""

class Heap(object):

    def __init__(self):
        self.capacity = 30
        self.size = 0
        self.items = [0 for _ in range(self.capacity)] 

    def left_child_index(self, parent_idx):
        return int(2*parent_idx+1)

    def right_child_index(self, parent_idx):
        return int(2*parent_idx+2)

    def parent_index(self, child_index):
        return int((child_index-1)/2)

    def has_left_child(self, idx):
        return self.left_child_index(idx) < self.size
    
    def has_right_child(self, idx):
        return self.right_child_index(idx) < self.size
    
    def has_parent(self, idx):
        return self.parent_index(idx) >= 0

    def left_child(self, idx):
        return self.items[self.left_child_index(idx)]
    
    def right_child(self, idx):
        return self.items[self.right_child_index(idx)]

    def parent(self, idx):
        return self.items[self.parent_index(idx)]

    def ensure_capacity(self):
        if self.size == self.capacity:
            new_items = [ 0 for _ in range(self.capacity*2) ]
            for i in range(self.size-1):
                new_items[i] = self.items[i]
            self.items = new_items
            self.capacity*=2
        
    def insert(self, item):
        self.ensure_capacity();
        self.items[self.size] = item
        self.size+=1
        self.heapify_up()

    def heapify_up(self):
        print("Heapifying up...")
        # Initial index
        idx = self.size-1
        print(">> Checking {} {}".format(
            self.items[idx], self.parent(idx) 
        ))
        while self.has_parent(idx) and self.parent(idx) < self.items[idx]:
            print("Checking {} => {} with {}".format(
                idx, self.items[idx], self.parent(idx)
            ))
            self.swap(idx, self.parent_index(idx))
            print("Swapping {} <=> {}".format(
                self.items[idx], self.parent(idx)
            ))
            idx = self.parent(idx)
    
    def heapify_down(self):
        idx = 0
        # Only left because if no left, no children
        while self.has_left_child(idx):
            # Get greater index
            greater_idx = self.left_child_index(idx)
            if self.has_right_child(idx) and self.right_child(idx) > self.left_child(idx):
                greater_idx = self.right_child_index(idx)
            
            # If there's nothing to swap...
            if self.items[idx] > self.items[greater_idx]:
                break
            else:
                self.swap(idx, greater_idx)
            idx = greater_idx

    def swap(self, idx, other_idx):
        tmp = self.items[idx]
        self.items[idx] = self.items[other_idx]
        self.items[other_idx] = tmp

    
        
if __name__=='__main__':
    heap = Heap()
    heap.insert(1)
    heap.insert(3)
    heap.insert(6)
    heap.insert(4)
    heap.insert(10)
    heap.insert(2)
    heap.insert(1)

    print(heap.items)