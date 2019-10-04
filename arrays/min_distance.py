""" Given two arrays, get the minimum
    difference between their elements

    Solution: 
    - Sort both array
    - set pointer to both arrays to 0
    - Increment where the move would minimize the distance
"""

arr1 = [3,7,1,9,10,43]
arr2 = [-10,100,22,30,12,40,42]

def min_dist(arr1, arr2):
    p1 = 0
    p2 = 0
    move = "p1"
    # Sort arrays
    arr1.sort()
    arr2.sort()
    print(arr1, arr2)
    # Loop to compare
    min_dist = None
    current_dist = None
    while p1 < len(arr1)-1 or p2 < len(arr2)-1:
        current_dist = abs(arr1[p1] - arr2[p2])
        print(arr1[p1], arr2[p2], min_dist, move)
        if not min_dist or current_dist < min_dist:
            min_dist = current_dist

        if p1 == len(arr1)-1:
            move = "p2"
        elif p2 == len(arr2)-1:
            move = "p1"
        else:
            # Check move where difference is least
            dist_p1 = abs(arr1[p1+1]-arr2[p2])            
            dist_p2 = abs(arr2[p2+1]-arr1[p1])
            move = "p1" if dist_p1 < dist_p2 else "p2"            
        # Move
        if move == 'p1' : p1+=1
        if move == 'p2' : p2+=1
    
    return min_dist

if __name__ == '__main__':
    print("Min distance of {} and {}".format(str(arr1), str(arr2)))
    dist = min_dist(arr1, arr2)
    print(dist)
        
