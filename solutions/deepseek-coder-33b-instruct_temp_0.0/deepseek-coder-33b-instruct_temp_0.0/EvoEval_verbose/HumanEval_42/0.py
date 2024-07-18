

def incr_list(l: list):
    """
    This function takes as input a list of integers and returns a new list where each element is incremented by 1.

    Parameters:
    l (list): A list of integers. This list can have any length, including 0, and the integers can be any valid integers.

    Returns:
    list: A new list containing the incremented values of the input list. The length of the output list will be the same as the input list, and the elements will be in the same order.

    Example usage:

    >>> incr_list([1, 2, 3])
    [2, 3, 4]

    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]