

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:  # Check if the list is empty
        return None  # Return None or raise an exception as per requirement
    max_val = l[0]  # Initialize max_val with the first element of the list
    for num in l:  # Iterate through the list
        if num > max_val:  # Compare current number with max_val
            max_val = num  # Update max_val if current number is greater
    return max_val  # Return the maximum value found
