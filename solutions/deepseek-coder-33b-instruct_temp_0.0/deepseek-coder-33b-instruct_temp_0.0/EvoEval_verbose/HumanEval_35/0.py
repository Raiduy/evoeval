

def max_element(l: list):
    """
    This function, 'max_element', is designed to find and return the maximum element in a given list. It takes one 
    argument, 'l', which is a list of elements. The function iterates through this list, comparing each element in order 
    to find the one with the highest value.
    
    Examples:
    
    If we pass [1, 2, 3] to the function as its input:
    >>> max_element([1, 2, 3])
    It will return 3, as 3 is the highest number in the list.
    
    If we pass [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10] to the function as its input:
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    It will return 123, as 123 is the highest number in the list.
    """
    if not l:
        return None
    max_val = l[0]
    for val in l:
        if val > max_val:
            max_val = val
    return max_val