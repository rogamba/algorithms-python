""" Sum two integers without using any
    arithmetic operators like + - * /
"""

def sum_bin(n1, n2):
    b1 = bin(n1)[2:]
    b2 = bin(n2)[2:]
    # zero fill to the largest
    largest = b1 if len(b1) > len(b2) else b2
    # Zfilling
    b1 = b1.zfill(len(largest)+1)
    b2 = b2.zfill(len(largest)+1)
    # Looping from right to left
    total = ''
    carrier = 0
    for i in range(len(largest), 0, -1):
        # Result
        if carrier == 0:
            if int(b1[i]) == 1 and int(b2[i]) == 1:
                res = 0
                carrier = 1
            elif int(b1[i]) == 1 or int(b2[i]) == 1:
                res = 1
                carrier = 0
            else:
                res = 0
                carrier = 0
        else:
            if int(b1[i]) == 1 and int(b2[i]) == 1:
                res = 1
                carrier = 1
            elif int(b1[i]) == 1 or int(b2[i]) == 1:
                res = 0
                carrier = 1
            else:
                res = 1
                carrier = 0
            
        # Prepend res
        total = "{}{}".format(res,total)
    # Last carrier
    total = "{}{}".format(carrier,total)
    return int(total,2)


if __name__ == '__main__':
    n1 = 15
    n2 = 3
    res = sum_bin(n1, n2)
    print("Sum of {} and {} without arithmetic ops is {}".format(
        n1, n2, res
    ))