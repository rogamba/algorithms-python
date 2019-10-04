""" Check if a string is contained
    in another string...
"""


from collections import deque

def is_substring(txt, sub):
    txt_map = {}
    # Create map
    for i in range(len(txt)):
        w = txt[i]
        if w not in txt_map:
            txt_map[w] = set()
        txt_map[w].add(i)
    # Check substring
    c = 0
    prev_idxs = []
    idxs = []
    # Get array of indexes
    for s in sub:
        if s not in txt_map:
            return False
        idxs.append(txt_map[s])

    # Loop and find path
    position = 1
    passed = idxs[0]
    while position < len(idxs):
        current = set()
        if len(passed) > 0:
            for idx in passed:
                if idx+1 in idxs[position]:
                    current.add(idx+1)
        else:
            return False
        passed = current.copy()
        position+=1

    # All passed
    return True
        
if __name__ == '__main__':
    txt = "este es un texto bien fuckin largo para probar qué tanto se puede alargar el sting contained"
    sub = "contained"
    print("Checking if '{}' is contianed in '{}'".format(
        sub, txt
    ))
    print(is_substring(txt, sub))
        

