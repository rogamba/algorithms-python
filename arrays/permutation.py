""" Check if string is permutation of other sting
"""
from collections import deque

def check_perm(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    # Implementation of stack
    stack = deque()
    for l in s2:
        stack.appendleft(l)
    # Build string
    perm = ""
    while len(stack) > 0:
        perm+=stack.popleft()
    # Check if equal
    return s1 == perm

if __name__ == '__main__':
    w1 = 'rodrigo'
    w2 = 'ogirdor'
    print(check_perm(w1,w2))


    