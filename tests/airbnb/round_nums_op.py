import math
import time

prices = [0.7,2.8,4.9,3.6,1.1,2.1,3.1,10.5,1.1,1.1,0.1,0.7,2.8,4.9,3.6,1.1,2.1,3.1,10.5,1.1,1.1,0.1]
target = 55
#prices = [0.5,1.5,0.5,1.5]
#target = 3

def round_nums(prices, target):
    min_error=None
    target_prices=[]
    # Rounded lists
    rounded_up = [ math.ceil(p) for p in prices ]
    rounded_down = [ math.floor(p) for p in prices ]
    reference_value = sum(prices)
    best_option = []
    min_error = None
    # Memoized list
    memo = set()

    def traverse_tree(down_idx=[], up_idx=[]):
        nonlocal min_error, best_option, prices, memo
        # Build the rounded arr
        rounded = [None for p in prices]
        error = 0
        for i in down_idx:
            rounded[i] = rounded_down[i]
            error+=abs(prices[i]-rounded_down[i])
        for i in up_idx:
            rounded[i] = rounded_up[i]
            error+=abs(prices[i]-rounded_up[i])
        # Check memo
        print(rounded)
        memo_idx = ":".join([ str(r) for r in rounded])
        # Base cases
        if sum(rounded) == target:
            if min_error == None or error < min_error:
                best_option = rounded
                min_error = error
            target_prices.append(rounded)
        # Starting with rounding down and then substituting
        for i, idx in enumerate(down_idx):
            # Adjust new indexes
            tmp_up_idx = up_idx[:]+[idx]
            tmp_down_idx = down_idx[:i]
            if len(down_idx) > 1:
                tmp_down_idx+=down_idx[i+1:]
            if memo_idx not in memo:
                traverse_tree(down_idx=tmp_down_idx, up_idx=tmp_up_idx)
            # Memoization
            #memo.add(memo_idx)

    traverse_tree(down_idx=[p for p in range(len(prices))], up_idx=[])
    print(target_prices)
    print(best_option)
    print(min_error)


if __name__ == '__main__':

    start = time.time()
    round_nums(prices, target)
    end = time.time()
    print("Executed in {}".format(end-start))

    