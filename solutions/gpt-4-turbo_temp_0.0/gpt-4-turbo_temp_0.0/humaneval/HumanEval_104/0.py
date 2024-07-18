
def unique_digits(x):
    """Given a list of positive integers x, return a sorted list of all 
    elements that haven't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # Filter the list to include only numbers with no even digits
    result = [num for num in x if all(int(digit) % 2 != 0 for digit in str(num))]
    
    # Return the sorted list
    return sorted(result)
