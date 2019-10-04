""" Recursion

    Write a method that prints all the subsets of a set
    
    Approach: 
    Given the set z = [a,b,c], all possible combinations are:
    subsets(z) = a+subsets([b,c])
"""

def powerset_recursion(arr, idx=0):
    """ Recursive solution for finding combinations
    """
    if len(arr) == idx:
        all_subsets = []
        # Append empty set
        all_subsets.append([])
    else:
        all_subsets = powerset_recursion(arr, idx+1)
        item = arr[idx]
        more_subsets = []
        # Cloning the subsets
        for subset in all_subsets:
            new_subset = []
            new_subset+=subset
            new_subset.append(item)
            more_subsets.append(new_subset)
        all_subsets+=more_subsets
    return all_subsets


def powerset_combinatorics(arr, combinations, memo={}):
    """ Iterate 2^n times, where n is the size of
        the set
    """
    all_subsets = []
    n = 2**len(arr)
    for i in range(n):
        subset = convert_to_set(i, arr)
        all_subsets.append(subset)
    return all_subsets


def convers_to_set(k, arr):
    """ Given the n^th combination, return  
        the set representation
    """
    subset = []
    idx = 0
    pass


def powerset_min(arr):
    subsets = []
    x = len(arr)
    print("Ranging {} to {}".format(x ,1 << x))
    for i in range(1 << x):
        s = []
        for j in range(x):
            print(i, 1 << j, i & (1 <<j ))
            if (i & (1 <<j )):
                s.append(arr[j])
        subsets.append(s)
        #subsets.append([ arr[j] for j in range(x) if (i & (1 << j))])
    return subsets


if __name__=='__main__':
    z=[1,2,3,4]
    print("Finding all subsets of : {}".format(z))
    subsets = powerset_min(z)
    print("Found {} powersets (representing 2^{} combinations): ".format(len(subsets), len(z)))
    for sub in subsets:
        print(sub)
