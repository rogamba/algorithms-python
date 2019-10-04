import sys
import json
from collections import deque
from pprint import pprint
""" Assume that you have location service that tells you all the sub-regions 
    that comprise the input region. For example, if you give the input 
    as "Earth", it will give you a list of all the continents in the 
    world, e.g. ["North America", "Europe", ...]. 
    Or if you put in "United States", it’ll return the states 
    ["California", "Oregon", ...].
 
    Given two regions, write a method that returns the smallest region that 
    includes both inputs. For example, "California" and "Mexico" should return 
    "North America". Or "San Francisco" and "Virginia" should return 
    "United States".
"""
# Class Region -> key, subregions, parent
# Use DFS to find both nodes 
# Compare the paths to both nodes
# Answer will be the right-most element of the intersection of both lists

def find_common_region(region1, region2):
    with open('regions.json') as file:
        earth = json.load(file)
    # Traverse and save the path to both nodes
    paths = {
        region1 : [],
        region2 : []
    }
    def find_path(target, region, path=[]):
        # Base cases
        if region['key'] == target:
            paths[target] = path
            return True
        if 'subregions' not in region:
            return False
        for reg in region['subregions']:
            find_path(target, reg, path=path[:]+[region['key']])
    # Both regions
    find_path(region2, earth)
    find_path(region1, earth)
    # Find find minimum_common
    i=0
    common = None
    while i < len(paths[region1]) and i < len(paths[region2]):
        if paths[region1][i] == paths[region2][i]:
            common = paths[region1][i]
        i+=1
    print("Common paths: ")
    print(common)
    return common

##############################
############# TEST ###########
##############################
print("#############################")
c1 = 'San Francisco'
c2 = 'Mexico'
min_common = find_common_region(c1, c2)
print("Min common region between {} and {} is {}".format(
    c1, c2, min_common
))



""" Define a class to encode the state of jigsaw, and use BFS to slove it.
"""



""" You’re given an array of CSV strings representing search  results. 
    Results are sorted by a score initially. 
    A given host may have several listings that show up in these results. 
    Suppose we want to show 12 results per page, but we don’t want the same 
    host to dominate the results. Write a function that will reorder the list 
    so that a host shows up at most once on a page if possible, but otherwise 
    preserves the ordering. Your program should return the new array and print 
    out the results in blocks representing the pages. 
    Sample Input: 
    [ 
        "host_id,listing_id,score,city", 
        "1,28,300.1,San Francisco", 
        "4,5,209.1,San Francisco", 
        "20,7,208.1,San Francisco", 
        "23,8,207.1,San Francisco", 
        "16,10,206.1,Oakland", 
        "1,16,205.1,San Francisco", 
        "1,31,204.6,San Francisco", 
        "6,29,204.1,San Francisco", 
        "7,20,203.1,San Francisco", 
        "8,21,202.1,San Francisco", 
        "2,18,201.1,San Francisco", 
        "2,30,200.1,San Francisco", 
        "15,27,109.1,Oakland", 
        "10,13,108.1,Oakland", 
        "11,26,107.1,Oakland", 
        "12,9,106.1,Oakland", 
        "13,1,105.1,Oakland", 
        "22,17,104.1,Oakland", 
        "1,2,103.1,Oakland", 
        "28,24,102.1,Oakland", 
        "18,14,11.1,San Jose", 
        "6,25,10.1,Oakland", 
        "19,15,9.1,San Jose", 
        "3,19,8.1,San Jose", 
        "3,11,7.1,Oakland", 
        "27,12,6.1,Oakland", 
        "1,3,5.1,Oakland", 
        "25,4,4.1,San Jose", 
        "5,6,3.1,San Jose", 
        "29,22,2.1,San Jose", 
        "30,23,1.1,San Jose" 
    ]
"""
# Loop the chunk of 12
# Init a set of hosts
# For every element in the list
# Check if it has reached page limit or is empty page
# Initialize page and set, check if there are duplicate values from last page
  # Duplicate values should be stored in order in a queue
  # Loop the duplicates, it there's more than one repeated in the dups, queue again for the next page
# Check element id if doesn't exist in the set of current page
# Append to the current page
# Repeat the process

def in_set(_id,_set):
    return True if _id in _set else False

def paginate():
    with open('results.json') as file:
        results = json.load(file)  
    # Loop results
    pages = []
    page = []
    duplicates = deque()
    for i, res in enumerate(results[1:]):
        result = res.split(",")
        if len(page) >= 12:
            pages.append(page)
            page = []
        # Reset page
        if len(page) <= 0:
            page = []
            set_ids = set()
            # Prepend records if unique
            for j in range(len(duplicates)):
                elem = duplicates.pop()
                if in_set(elem[0],set_ids):
                    duplicates.appendleft(elem)
                else:
                    page.append(elem)
                    set_ids.add(elem[0])
        # Check set
        if in_set(result[0], set_ids):
            duplicates.appendleft(result)
        else:
            page.append(result)
            set_ids.add(result[0])
    return pages

##############################
############# TEST ###########
##############################    
pages = paginate()
pprint(pages)


""" Study threads, deadlocks and mutexes
    - Variation of string reversal
    - Knapsack
"""


""" Modified version of the traditional "change-making" problem with the 
    coins as items priced in floats and a target sum needed to reach.

    Given an array of float prices, round each price such that the total 
    sum of the prices stays as close as possible to the previous sum but 
    the prices in the array are converted to round numbers 
    IE (36.46 4.54) will become (36, 5)

    Given a list of nodes and a list of directed connections each one of those 
    nodes has to each other(not every node has a connection, and cycles may exist), 
    find the minimal amount of entry points for a message to spread to every node.

    "Word search II" on leetcode but with determining the largest number of words 
    you can pack onto the graph at any one time.

"""
CHANGE = 10
denominations = [25,10,5,1]
combos = []

def combinations(n, path=''):
    if path!='':
        sum_path = sum([ int(i) for i in path[:-1].split(":")])
    else:
        sum_path = 0
    # Loop denominations
    for den in denominations:
        # Copy array cause it's passed by reference
        if n-(sum_path+den) == 0:
            combos.append(path+"{}:".format(den))
        elif n-(sum_path+den) > 0:
            # Recursive call
            combinations(n, path+"{}:".format(den))
    return path

##############################
############# TEST ###########
##############################
print("#############################")
print("Getting combinations of {}".format(CHANGE))
combinations(CHANGE)
print("----")
print(len(combos))
print(combos)



""" Iterator class
    - has_next
    - next
    - remove
"""
class Iterator(list):
    def __init__(self, data):
        self.p = 0
        self.ps = 0
        for d in data:
            self.append(d)
    def has_next(self):
        if self.p >= len(self)-1 and self.ps >= len(self[-1])-1:
            return False
        return True
    def next(self):
        # Increment
        while len(self[self.p]) <= 0 or self.ps >= len(self[self.p]):
            self.p+=1
            self.ps=0
        # return
        val = self[self.p][self.ps]
        self.last = (self.p, self.ps) 
        self.ps+=1
        return val
    def remove(self):
        # Remove and displace elements
        tmp = []
        for i in range(len(self[self.last[0]])):
            if i != self.last[1]:
                tmp.append(self[self.last[0]][i])
        self[self.last[0]] = tmp 
        self.p, self.ps = self.last

print("#############################")
print("Iterator:")
it = Iterator([[],[1,2,3],[],[4,5],[],[6]])
while it.has_next():
    print(it.next())
it.remove()
print(it)
        
