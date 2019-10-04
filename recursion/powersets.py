""" Given  list or set, find all the possible
    subsets.
    e. (ABCD) => [
        (A),(B),(C),(D),
        (AB),(AC),(AD),(BC),(BD),(CD)
        (ABC),(ABD),(ACD),(BCD)
    ]
"""

# elimination tree

def powersets(arr):
    sets = []
    analyzed = set()
    def get_by_elimination(lst):
        if lst in analyzed:
            return
        analyzed.add(lst)
        # Base case
        if len(lst) <= 1:
            return lst
        for i in range(len(lst)):
            sub = lst[:i] + lst[i+1:]
            if sub not in sets:
                sets.append(sub)
            get_by_elimination(sub)
    get_by_elimination(arr)        
    return sets

if __name__ == '__main__':
    arr = ("A","B","C","D")
    sets = powersets(arr)
    print(sets)