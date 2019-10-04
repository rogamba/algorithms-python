""" Min distance between words in text
"""

def get_min_distance(arr1, arr2):
    # We assume arr1 and arr2 are always sorted
    min_error = None
    p1 = 0
    p2 = 0
    while p1 < len(arr1) or p2 < len(arr2):
        # Check the current error
        error = abs(arr1[p1]-arr2[p2])
        if min_error == None or error < min_error:
            min_error = error
        # Move the pointer to the one that gives less distance
        error_p1, error_p2 = None, None
        if p1 < len(arr1)-1:
            error_p1 = abs(arr1[p1+1] -arr2[p2])
        if p2 < len(arr2)-1:
            error_p2 = abs(arr1[p1] -arr2[p2+1])
        # Move
        if error_p1 != None and error_p2 != None:
            p1 = p1+1 if error_p1 < error_p2 else p1
            p2 = p2+1 if error_p2 < error_p2 else p2
        elif error_p1 == None and error_p2 != None:
            p2+=1
        elif error_p2 == None and error_p1 != None:
            p1+=1
        else:
            break
        
    return min_error

def min_word_distance(txt, w1, w2):
    """ Get minimum distance between words
    """
    word_arr = txt.split(" ")
    word_map = {}
    # Create word map
    for i, word in enumerate(word_arr):
        if word == w1 or word == w2:
            if word not in word_map:
                word_map[word] = []
            word_map[word].append(i)
    # the two words were not found
    if len(word_map) < 2:
        return False
    # Get minimum distance between arrays
    print(word_map)
    min_distance = get_min_distance(word_map[w1],word_map[w2])
    return min_distance


txt = "es este es un texto que esta muy largo para ver que pex con muy muy muy las distancias muy grandes es largo"
w1 = "es"
w2 = "largo"
#dist = min_word_distance(txt,w1,w2)
#print(dist)


##################################################
##################################################
##################################################


""" Check if string is substring of another
    Options of solution:
    - lettermap
    - backtracking
    - path of indexes
"""

def check_substring(str1, str2):
    # Map all the letters of the substring 
    word_map = {}
    for i,l in enumerate(str1):
        if l in str2:
            if l not in word_map:
                word_map[l] = set()
            word_map[l].add(i)
    # Check if is subset
    if set(str2) != set(word_map.keys()):
        return False
    # Check path
    prev = None
    c = 1
    for l in str2:
        idx = word_map[l]
        if prev == None:
            prev = list(idx)
            continue
        current = []
        if prev:
            c+=1
            for i in prev:
                if i+1 in idx:
                    current.append(i+1)
        prev = current
    contained = c == len(str2)
    print(contained)
    return contained


#check_substring("parangaricutirimicuaro","para")

##################################################
##################################################
##################################################

class LinkedList(object):
    def __init__(self):
        self.head = None
    class Node:
        def __init__(self, data=None):
            self.data=data
            self.nxt=None
    def __str__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.nxt
        return "->".join(nodes)
    def add(self, data):
        if not self.head:
            self.head = self.Node(data)
            return 
        curr = self.head
        while curr.nxt:
            curr = curr.nxt
        curr.nxt = self.Node(data)
    def reverse_inplace(self):
        curr = self.head
        c = 0
        # New attribute
        prev = None
        while curr:
            curr.new_nxt = prev
            prev = curr
            if curr.nxt == None:
                break
            curr = curr.nxt
        # Shitch attributes
        self.head = curr
        while curr:
            curr.nxt = curr.new_nxt
            curr = curr.nxt
        # Loop to remove the attribute
        curr = self.head
        while curr.nxt:
            curr.new_nxt = None
            curr = curr.nxt
            

def build_ll():
    ll = LinkedList()
    last = ll
    for i in range(10):
        ll.add(i)
    print(ll)
    return ll

lst = build_ll()
print(lst)
lst.reverse_inplace()
print(lst)
lst.reverse_inplace()
print(lst)
#rev = list_reversal(lst)


##################################################
##################################################
##################################################

def make_change(coins, target=0):
    combos = set()
    def make_combo(change=[], total=0):
        if total == target:
            combos.add(tuple(change))
        if total > target:
            return
        # Recurse
        for i,c in enumerate(coins):
            new_change = change[:]
            new_change[i]+=1
            new_total=total+c
            if new_total <= target:
                check_change = tuple(new_change)
                if check_change not in combos:
                    make_combo(new_change, total=new_total)   
    # Make the change
    change = [0 for _ in coins]
    make_combo(change=change)
    return combos

coins = [20,10,5,2,1]
target = 15
combos = make_change(coins, target)
print(combos)


##################################################
##################################################
##################################################

