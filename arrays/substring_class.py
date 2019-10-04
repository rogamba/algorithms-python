""" Check if string is contained
    in another string
"""
from collections import deque

class SuperString(str):

    def __init__(self, txt):
        pass

    def contains(self, txt):
        """ Brute force
        """
        supertext = []
        for r in self.__iter__():
            supertext.append(r)
        subtext = []
        for s in txt.__iter__():
            subtext.append(s)

        # Starting points indeces
        starting_points = []
        for i in range(0,len(supertext)):
            if supertext[i] == subtext[0]:
                starting_points.append(i)
        
        # From starting points iterate
        for start in starting_points:
            sup_idx = start
            sub_idx = 0
            test = []
            while supertext[sup_idx] == subtext[sub_idx]:
                test.append(supertext[sup_idx])
                sup_idx+=1
                sub_idx+=1
                if test == subtext:
                    return True
                if sub_idx >= len(subtext) or sup_idx >= len(supertext):
                    break
                    
        return False

    def contains_optimal(self, txt):
        """ With a double ended queue
            and two pointers
            Rocola  ==  ola
             |   |
        """
        supertext = []
        for r in self.__iter__():
            supertext.append(r)
        subtext = []
        for s in txt.__iter__():
            subtext.append(s)

        p_head = 0
        p_tail = len(txt)

        original = deque(subtext)
        compare = deque(supertext)

        while len(compare) > 0:
            # Compare head
            while supertext[p_head] != subtext[0]:
                p_head+=1
                compare.popleft()
                if p_head >= len(supertext):
                    return False
            # Compare tail
            print(supertext[p_tail],subtext[len(subtext)-1])
            while supertext[p_tail] != subtext[len(subtext)-1]:
                print("---")
                p_tail-=1
                compare.pop()
                if p_tail <= 0:
                    return False
            # Compare
            print(original, compare)
            if original == compare:
                return True

        return False



if __name__=='__main__':
    text1 = SuperString('ASDaRodrigoalALSd')
    text2 = SuperString('Rodrigo')
    print("Checking if {} is contained in {}?".format(
        text2, text1
    ))
    print(text1.contains(text2))
    print(text1.contains_optimal(text2))


    