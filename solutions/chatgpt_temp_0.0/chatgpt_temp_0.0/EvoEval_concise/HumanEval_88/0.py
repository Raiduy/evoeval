
def sort_array(array):
    """
    Returns a sorted copy of the input array with non-negative integers. If the sum of the first and last elements is odd, sorts the array in ascending order. 
    If the sum is even, sorts the array in descending order. The original array remains unchanged.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    sorted_array = sorted(array)
    if len(sorted_array) < 2:
        return sorted_array
    if (sorted_array[0] + sorted_array[-1]) % 2 == 0:
        return sorted_array[::-1]
    else:
        return sorted_array