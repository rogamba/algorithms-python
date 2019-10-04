coins = [25, 10, 5, 1]
target = 10

# Ways to make the target
def make_change(target, coins):
    combinations = []
    memo = set()
    def _make_change(total=0,path=[],hmap={}):
        nonlocal combinations
        # Memoization
        s= ":".join( ["{}x{}".format(c,hmap[c]) for c in coins] )
        if s in memo:
            return
        else:
            memo.add(s)
        # Base case
        if total == target:
            combinations.append(path)
            return
        for coin in coins:
            new_total = total+coin
            new_hmap = hmap.copy()
            new_hmap[coin] = hmap[coin]+1
            if new_total <= target:
                _make_change(total=new_total,path=path[:]+[coin],hmap=new_hmap)
    
    hmap = {c:0 for c in coins}
    _make_change(total=0, path=[], hmap=hmap)
    return combinations


combos = make_change(target, coins) 
print(combos)