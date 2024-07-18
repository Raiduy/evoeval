
def next_smallest(lst):
    """
    Given a list of integers, return the second smallest element. If no such element exists, return None.
    
    Examples: 
    next_smallest([1, 2, 3, 4, 5]) -> 2
    next_smallest([5, 1, 4, 3, 2]) -> 2
    next_smallest([]) -> None
    next_smallest([1, 1]) -> None
    """
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return None
    unique_lst.sort()
    return unique_lst[1]