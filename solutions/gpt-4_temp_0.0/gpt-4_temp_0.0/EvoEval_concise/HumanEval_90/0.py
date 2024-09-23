
def next_smallest(lst):
    """
    Given a list of integers, return the second smallest element. If no such element exists, return None.
    
    Examples: 
    next_smallest([1, 2, 3, 4, 5]) -> 2
    next_smallest([5, 1, 4, 3, 2]) -> 2
    next_smallest([]) -> None
    next_smallest([1, 1]) -> None
    """
    if len(lst) < 2:
        return None
    else:
        lst = list(set(lst))
        if len(lst) < 2:
            return None
        else:
            lst.sort()
            return lst[1]