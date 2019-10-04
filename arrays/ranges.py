""" In an array of 1s and 0s print the
    ranges of the 1s
    In: [1,1,0,1,0,1,1,1,0,0,1]
    Out:1-2,4,6-8
"""

arr = [1,1,0,1,0,1,1,1,0,0,1]

def get_ranges(arr):
    idxs = []
    for i in range(len(arr)):
        if arr[i]:
            idxs.append(i+1)
    print(idxs)
    # Arrange the indexes
    ranges=[]
    ranges_string = []
    ps = 0
    pe = 0 
    while ps < len(idxs):
        print(ranges)
        pe=ps+1
        n=1
        while pe < len(idxs) and idxs[ps]+n == idxs[pe]:
            n+=1
            pe+=1
        # Append the range
        _range = "{}".format(idxs[ps])
        if idxs[ps] != idxs[pe-1]:
            _range+="-{}".format(idxs[pe-1])
        ranges.append(_range)
        ps=pe

    print(ranges)
    return ranges

get_ranges(arr)