""" Given a number n, find all the prime
    numbers that are lower than n

    start from the smallest numbers
    and check if they are primes, if they
    are, remove all its multiples from
    the array until n

"""

def find_primes(n):
    # Builf array of possible numbers
    arr = [False, False] + [ True for i in range(2,n)]

    for i in range(0,len(arr)):
        # If its prime, set to false all the others
        if arr[i] == True:
            print("Checking {}".format(i))
            c = i**2
            for c in range(c,n,i):
                print("Removing {}".format(c))
                arr[c] = False

    nums = []
    for i in range(len(arr)):
        if arr[i]:
            nums.append(i)

    return nums


if __name__ == '__main__':
    arr = find_primes(100)
    print(arr)

