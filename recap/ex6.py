""" Volume of histogram:
    Calculate the total amount of water that a
    histogram graph can hold if poured water on top

    |
    |                   |..........
    |    ...............|         | 
    |    |              |         |
    |    |    |         |    |    | 
    |____|____|_________|____|____|_________>

    Ex: [2,1,0,4,1,3,0,0]

"""

#histogram = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
histogram = [0,4,6,0,5,2,0,0,3,0,0,0]

def calculate_vol(histo):
    # Boundries
    b_start = None
    b_end = None
    current_boundry = None
    
    boundries = []
    p = 0

    # Loop
    while p < len(histo):
        if histo[p] <= 0:
            p+=1
            continue
        max_pos = None
        max_boundry = None
        cont = False
        for i in range(p+1,len(histo)):
            if max_boundry == None:
                max_boundry = histo[i]
            if histo[i] >= max_boundry:
                max_boundry = histo[i]
                max_pos = i
            if histo[p] < histo[i]:
                boundries.append((histo[p],histo[i]))
                p=i
                cont = True
                break
        if cont:
            continue
        boundries.append((histo[p],histo[max_pos]))
        p = max_pos
    
    return boundries


if __name__ == '__main__':
    calculate_vol(histogram)
