""" Check hoy many people can seat down
    in a cinema seats row given the constain that one 
    can only seat down if both of the extremes are 0
"""

# row = [1, 0, 0, 1, 0, 0]
# n 
 
# [1,0,1,0,1,0,x,0,1,0,x,0,x]  (distribución inicial)
# n = 3 (adicionales)
 
 
# Test cases
assert is_available([1, 0, 1], 1) is False
assert is_available([0, 0, 0], 2) is True