

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)  # Sort the list
    n = len(sorted_list)
    
    if n % 2 == 1:  # If the list has an odd number of elements
        return sorted_list[n // 2]
    else:  # If the list has an even number of elements
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
