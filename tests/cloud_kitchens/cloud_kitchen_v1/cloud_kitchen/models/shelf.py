class Shelf(Object):
    """ Abstract class to build the
        concrete shelve classes which are
        implemented as queues
    """
    def pop_by_id(id: int) -> Order:
        pass
    
    def push(order: Order):
        pass
    
    def get_next() -> []Orders:
        pass
