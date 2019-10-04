""" Maximize the profix given a set of objects and a maximum
    capacity of weight
"""

P = [1,2,5,6]
W = [2,3,4,5]
n = 4
m = 8

def get_best_combo():
    P_per_W = [P[i]/W[i] for i in range(len(P))]
    max_profit = 0
    combo = []

    def explore(path=set(), sum_profit=0, sum_weight=0):
        nonlocal combo, max_profit
        # Base cases
        if sum_weight <= m:
            if sum_profit > max_profit:
                max_profit = sum_profit
                combo = path
        # NO more left to traverse
        if len(path) >= len(P) or sum_weight > m:
            return
        for i in range(len(P)):
            if i not in path:
                new_path = path.copy()
                new_path.add(i)
                explore(
                    path=new_path, 
                    sum_profit=sum_profit+P[i],
                    sum_weight=sum_weight+W[i]
                )
        return

    # Indexes
    explore()
    exists = [0 for i in range(len(P))]
    for i in combo:
        exists[i] = 1
    
    print(exists)
    return exists


if __name__ == '__main__':
    get_best_combo()


