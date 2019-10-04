""" Given a large text file containing words.
    Given any two words, find the shortest distance 
    (in terms of words) between them in the file. If the
    operation will be repeated many times for the same 
"""

# Scan chunk of file
# Increment counter for every word
# Store counter of both words and
# Optimize creating a map of word -> indexes

text=[
    "hola este es un texto bien chido para probar que sirve este pedo que sirve para estudiar"
]

def find_shortest(arr1, arr2):
    p1, p2 = 0, 0
    move = None
    min_distance = None
    current_distance = None
    while p1 < len(arr1) or p2 < len(arr2):
        current_distance = abs(arr1[p1] - arr2[p2])
        print(arr1[p1], arr2[p2])
        # Min distance
        if not min_distance or current_distance < min_distance:
            min_distance = current_distance
        if p1 == len(arr1)-1 and p2 == len(arr2)-1:
            break
        if p1 == len(arr1)-1:
            move = 'p2'
        elif p2 == len(arr2)-1:
            move = 'p1'
        else:
            # Check where to move
            d1 = abs(arr1[p1+1]-arr2[p2])
            d2 = abs(arr1[p1]-arr2[p2+1])
            move = 'p1' if d1 > d2 else 'p2'
        # Move
        print("Move ", move)
        if move == 'p1' : p1+=1
        if move == 'p2' : p2+=1
    return min_distance


def find_distance(w1, w2):
    global text
    c=0
    word_idx = {w1:[], w2:[]}
    for line in text:
        line_words = line.split(" ")
        for word in line_words:
            c+=1
            if word in word_idx:
                word_idx[word].append(c)
                
    # Not found
    if len(word_idx[w1]) <= 0 or len(word_idx[w2]) <= 0:
        return False
    # Shortest distance
    print(word_idx)
    shortest = find_shortest(word_idx[w1], word_idx[w2])
    return shortest


if __name__ == '__main__':
    w1 = 'este'
    w2 = 'pedo'
    min_dist = find_distance(w1, w2)
    print("Min distance is: {}".format(min_dist))
                