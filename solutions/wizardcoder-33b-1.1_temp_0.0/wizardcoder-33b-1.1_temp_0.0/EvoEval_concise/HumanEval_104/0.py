
def unique_digits(x):
    """Returns a sorted list of integers from the input list x that do not contain any even digits.

    The list is sorted in ascending order.
    
    Example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    result = []
    for num in x:
        if all((digit % 2 != 0 for digit in map(int, str(num)))):
            result.append(num)
    return sorted(result)