
def sort_array(arr):
    """
    Sort an array of non-negative integers based on the number of ones in their binary representations in ascending order.
    If two integers have the same number of ones, sort them based on their decimal values.

    Example:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    """
    ones_count = [bin(num).count('1') for num in arr]
    sorted_arr = sorted(arr, key=lambda x: (ones_count[x], x))
    return sorted_arr