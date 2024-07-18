

def max_element(l: list):
    """Finds and returns the largest number in a list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_num = l[0]
    for num in l[1:]:
        if num > max_num:
            max_num = num
    return max_num