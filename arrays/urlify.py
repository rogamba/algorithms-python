""" Given a string, substitute all
    spaces for %20 characters, assume 
    the length of the array has enough 
    space.

    Mr John Smith
    Mr%20John%20Smith

"""

def urlify(txt):
    # Loop and copy elements
    txt = list(txt)
    i=0
    while i < len(txt)-1:
        if txt[i] != ' ':
            i+=1
            continue
        # Make room
        txt.append(None)
        txt.append(None)
        for idx in range(len(txt)-3,i,-1):
            tmp = txt[idx]
            txt[idx+2] = tmp
        # Insert
        txt[i] = '%'
        txt[i+1] = '2'
        txt[i+2] = '0'
        i+=1
    
    s = ''
    for l in txt:
        s+=l
    
    return s

if __name__ == '__main__':
    txt = "Este es un texto bien chido para el urlify"
    print(urlify(txt))