""" Powersets
"""

def powersets(arr):
    powersets = set()
    def _powersets(arr):
        # Base cases
        print(arr)
        nonlocal powersets
        pset = set(arr)
        powersets.add(arr)
        # Recursion
        for i in range(len(arr)-1):
            new_arr = arr[:i]+arr[i+1:]
            new_set = set(new_arr)
            if new_arr not in powersets:
                _powersets(new_arr)

    _powersets(arr)
    return powersets

if __name__ == '__main__':
    arr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q')
    psets = powersets(arr)
    print(len(psets))
