""" Given two strings write a method
    to check if one string is a rotation (reversed)
    of the other. You can assume there is a 
    methos is_substring() that returns True if the
    string is contained in another string. You can call
    this methos only once
"""
from collections import deque

string = "watterbottle"
rotated = "erbottlewatt"
r2 = "aterbottlew"
r3 = "ewatterbottl"


def check_rotation(txt, rotated):
    d1 = deque(txt)
    d2 = deque(rotated)
    # Not same length
    if len(d1) != len(d2):
        return False
    # Rotate and evaluate
    for i in range(len(rotated)):
        print(d2)
        if d1 == d2:
            return True
        tail = d2.pop()
        d2.appendleft(tail)
    return False


def check_rotation_optimal(txt, rotated):
    if len(txt) != len(rotated):
        return False    
    check = rotated + rotated
    return is_substring(txt, check)


if __name__ == '__main__':
    print("Checking rotation for {} {}".format(
        string, rotated
    ))
    print(check_rotation(string, rotated))

    