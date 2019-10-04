""" Amz interview problem 2 
"""

def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):

    combinations = []
    min_comb = None
    min_diff = None

    for f_id, f in forwardRouteList:
        for r_id, r in returnRouteList:
            diff = maxTravelDist - (f+r)
            if diff < 0:
                continue
            combinations.append( ([f_id, r_id], diff) )

    if len(combinations) <= 0:
        return []

    # Order Tuple by distance
    ordered = sorted(combinations, key= lambda elem: elem[1])
    
    # Return only the mins
    min_diff = ordered[0][1]
    min_combs = []
    for comb, diff in ordered:
        if diff == min_diff:
            min_combs.append(comb)

    return min_combs



if __name__=='__main__':
    m = 10000
    f = [
        (1,3000),
        (2,5000),
        (3,7000),
        (4,10000),
    ]
    r = [
        (1,2000),
        (2,3000),
        (3,4000),
        (4,5000)
    ]
    res = optimalUtilization2(m,f,r)
    print(res)
    pass