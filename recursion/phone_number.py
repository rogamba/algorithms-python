""" Given a length of a phone number, find all
    possible combinations of phones that can exist

    the possible combinations will be

    We can solve it thinking in a tree-like structure:
    Where the depth is the length of the phone number. 

                        0 ...       
            0 ...               9
    0 1 2 3 4 5 6 7 8 9

    Therefore all possible combinatinos will be:
    
                10^(depth)

"""

n=4

def find_combinations(n):
    nums = list(range(0,10))
    combinations = []

    def get_phone_number(path=""):
        # Base case: get combination and return
        if len(path) == n:
            combinations.append(path)
            return
        for num in nums:
            get_phone_number(path=path+str(num))
    
    get_phone_number()
    return combinations

combos = find_combinations(n)
print(combos)