
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # Remove duplicates from the list
    lst = list(set(lst))
    
    # Check if the list has at least 2 elements
    if len(lst) < 2:
        return None
    
    # Sort the list in ascending order
    lst.sort()
    
    # Return the second smallest element
    return lst[1]
