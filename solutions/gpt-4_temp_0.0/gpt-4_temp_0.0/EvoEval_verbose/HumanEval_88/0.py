
def sort_array(array):
    """
    This function takes as input an array composed of non-negative integers. The function will then return another array, 
    which is a sorted copy of the original array. The sorting order is determined by the sum of the first and the last element of the given array.
    
    If the sum of the first and the last element is an odd number, the function will sort the array in ascending order. Conversely, if the sum is an even number,
    the function will sort the array in descending order. 

    It is important to note that this function does not alter the original array - it only provides a sorted copy.

    Parameters:
    array (list): A list of non-negative integers.

    Returns:
    list: A sorted copy of the original list. The sorting is in ascending order if the sum of the first and last elements is odd,
    and in descending order if this sum is even.

    Examples:
    * sort_array([]) => [] - Empty list is returned as there are no elements to sort.
    * sort_array([5]) => [5] - Single-element list is returned as is, as there is no scope for sorting.
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5] - List is sorted in ascending order as sum of first and last element (2+5=7) is odd.
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0] - List is sorted in descending order as sum of first and last element (2+6=8) is even.
    """
    if len(array) < 2:
        return array
    else:
        sum = array[0] + array[-1]
        if sum % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)