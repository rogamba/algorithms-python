""" Amz
"""

def is_numeric(txt):
    n = txt[0]
    try:
        int(n.replace(' ',''))
        return True
    except:
        return False


def prioritizedOrders(numOrders, orderList):
    """ Array of ids, and those ids refer to
        keys in a hashtable...
    """
    if len(orderList) != numOrders:
        return False
    # WRITE YOUR CODE HERE
    orders = {}
    arr_ids = []
    arr_meta = []

    orders_prime = []
    orders_normal = []

    for i in range(0,numOrders):
        # Data array
        data = orderList[i].split(' ')
        order_id = data[0]
        # Metadata
        metadata = " ".join(data[1:])
        # Store in hastable
        orders[order_id] = orderList[i]
        # Check if it's a prime order
        if is_numeric(metadata):
            orders_normal.append((metadata, order_id))
        else:
            orders_prime.append((metadata,order_id))

    # Sort the prime orders first by metadata, then by
    # order id
    result=[]
    prime_sorted = sorted(orders_prime, key= lambda elem: (elem[0], elem[1]))

    # Reduce orders
    for meta,id in prime_sorted:
        result.append("{} {}".format(id, meta))
    for meta,id in orders_normal:
        result.append("{} {}".format(id, meta))

    return result

    
if __name__=='__main__':
    orders = [
        't2 13',
        'f3 52',
        'r1 box ape',
        'br8 eat',
        'w1 has'
    ]
    res = prioritizedOrders(5,orders)
    print(res)
    pass