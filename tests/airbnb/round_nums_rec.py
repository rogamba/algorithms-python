import math
import time

prices = [0.7, 2.8, 4.9, 3.6,1.1,2.1,3.1,10.5,1.1,1.1,0.1,0.7, 2.8,4.9,3.6,1.1,2.1,3.1,10.5,1.1,1.1,0.1]
target = 55

def roundNumbers(prices, target):
    # Round
    target_combos = []
    global_min = None
    memo = set()

    def find_paths(idx=0,total=0,error=0,path=[]):
        nonlocal global_min, memo
        # Target is overpassed
        if idx >= len(prices):
            if sum(path) == target:
                target_combos.append((path,error))
                if global_min == None or error < global_min[1]:
                    global_min = (path, error)
            return
        price = prices[idx]
        price_up = math.ceil(price)
        price_down = math.floor(price)
        # Recurse combinations
        for rounded in [price_down, price_up]:
            memo_code = "{}:{}".format(len(path),rounded)
            if memo_code not in memo:
                t, e, p = total+rounded, error+abs(price-rounded), path[:]+[rounded]
                find_paths(
                    idx+1, 
                    total=t,
                    error=e,
                    path=p)
                memo.add(memo_code)

    # Find paths
    find_paths()
    # No paths to target were found...
    if len(target_combos) <= 0:
        return False
    # Sort by minimal error
    return target_combos[0]

if __name__ == '__main__':
    start = time.time()
    rounded_nums, error = roundNumbers(prices, target)
    end = time.time()
    print("Prices: {}".format(prices))
    print("Target: {}".format(target))
    print("---------")
    print("Result set: {}".format(rounded_nums))
    print("Error: {}".format(error))
    print("Executed in {}".format(end-start))
