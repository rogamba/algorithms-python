""" Given a list of numbers and letters,
    find the longest subarray with the same
    amount of letters and numbers
"""

a = 'a'
arr=[a,1,1,1,1,a,a,a,1,a,1,1,1,1,1,1,1,1,1,a]


def get_longest_equal_rec(arr):
    count = {
        "l" : 0,
        "n" : 0
    }
    equal_subsets = []
    memo = set()
    max_subset = []

    # Count
    for a in arr:
        t = 'n' if type(a) == int else 'l'
        count[t]+=1

    def _get_subsets(arr,n=0,l=0):
        nonlocal equal_subsets, max_subset
        # Base case
        if len(arr) == 0 or tuple(arr) in memo:
            return

        # Append to subsets only if the n == l
        print(n, l, arr)
        memo.add(tuple(arr))
        if n == l:
            if len(arr) > len(max_subset):
                max_subset = arr
            equal_subsets.append(arr)

        # Recurse adjacent nodes
        adj_left = arr[1:]
        adj_right = arr[:-1]

        # New left and right count
        type_l = 'n' if type(arr[0]) == int else 'l' 
        type_r = 'n' if type(arr[-1]) == int else 'l' 

        # New number
        new_left_n = n-1 if type_l == 'n' else n
        new_left_l = l-1 if type_l == 'l' else l

        new_right_n = n-1 if type_r == 'n' else n
        new_right_l = l-1 if type_r == 'l' else l

        # Recurse
        _get_subsets(adj_left, n=new_left_n, l=new_left_l)
        _get_subsets(adj_right, n=new_right_n, l=new_right_l)

    _get_subsets(arr, n=count['n'],l=count['l'])

    return max_subset

            
if __name__ == '__main__':
    print("Getting longest subsequence of equal number of letters and numbers for the set:")
    print(arr)
    sub = get_longest_equal_rec(arr)
    print("Subset:")
    print(sub)