# Change making
coins = [25,10,5,2,1]
n = 10

def make_change(coins, target):
    paths = []
    memo = set()

    def explore_paths(total, combo={}):
        nonlocal paths
        # Base cases
        if total > target:
            return False
        if total == target:
            paths.append(combo)
        # Recursion
        for coin in coins:
            # New combo to send
            new_combo = combo.copy()
            new_combo[coin]+=1
            # memo code
            combo_code = ":".join(
                ["{}x{}".format(c,q) for c,q in new_combo.items()]
            )
            # Check if not in memo
            if combo_code not in memo:
                memo.add(combo_code)
                explore_paths(total=total+coin,combo=new_combo)
    
    combo_init = {coin:0 for coin in coins}
    explore_paths(0, combo_init)

    return paths

if __name__ == '__main__':
    combos = make_change(coins, n)
    print(len(combos))
        