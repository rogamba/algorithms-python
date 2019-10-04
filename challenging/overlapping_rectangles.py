""" Given two rectangles, find the overlapping 
    rectangle.
    - Rectangles given by two coords
    - Find coords of overlapping rectangle
"""

class Rectangle(object):
    def __init__(self, c1=None, c2=None):
        if c1 == None or c2 == None:
            return
        # Find coords
        if c1[0] <= c2[0]:
            left = c1[0]
            right = c2[0]
        else:
            left = c2[0]
            right = c1[0]
        # Find coords
        if c1[1] <= c2[1]:
            bottom = c1[1]
            top = c2[1]
        else:
            bottom = c2[1]
            top = c1[1]
        # Boundried
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top

    def __str__(self):
        return "Rectangle({},{},{},{})".format(
            self.left, self.right, self.bottom, self.top
        )

def find_overlapping(r1, r2):
    # Overlapping in x axis
    leftmost = r1 if r1.left < r2.left else r2
    other = r2 if leftmost == r1 else r1
    if leftmost.right < other.left:
        return None

    overlap_left = other.left
    overlap_right = other.left + (other.right-other.left) - (0 if other.right < leftmost.right else other.right-leftmost.right)

    # Overlapping in y axis
    bottom = r1 if r1.bottom < r2.bottom else r2
    other = r2 if bottom == r1 else r1
    if bottom.top < other.bottom:
        return None

    overlap_bottom = other.bottom
    overlap_top = other.bottom + (other.top-other.bottom) - (0 if other.top < leftmost.top else other.top-bottom.top)

    # Both have to fulfill the condition of overlapping
    if overlap_top < 0 or overlap_left < 0:
        return 0

    return Rectangle((overlap_left,overlap_bottom),(overlap_right, overlap_top))



if __name__ == '__main__':

    #Overlapping
    r1 = Rectangle((1,1), (10,10))
    r2 = Rectangle((3,3), (6,6))

    # None overlapping
    r3 = Rectangle((1,6), (2,7))
    r4 = Rectangle((7,1), (8,3))
    
    overlapping = find_overlapping(r1, r2)

    print("Finding overlapping rectangle")
    print(overlapping)