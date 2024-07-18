

def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Check if the list is monotonically increasing
    increasing = all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    # Check if the list is monotonically decreasing
    decreasing = all(l[i] >= l[i + 1] for i in range(len(l) - 1))
    
    # Return True if either condition is met
    return increasing or decreasing
