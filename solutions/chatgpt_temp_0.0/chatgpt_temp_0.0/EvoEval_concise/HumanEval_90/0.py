
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
    smallest = float('inf')
    second_smallest = float('inf')
    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest