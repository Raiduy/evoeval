
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    # Copy the given array to avoid changing it
    array_copy = array.copy()
    
    # Check if the array is empty or contains only one element
    if len(array_copy) <= 1:
        return array_copy
    
    # Calculate the sum of the first and last elements
    sum_first_last = array_copy[0] + array_copy[-1]
    
    # Sort the array based on the condition
    if sum_first_last % 2 == 0:  # If the sum is even, sort in descending order
        array_copy.sort(reverse=True)
    else:  # If the sum is odd, sort in ascending order
        array_copy.sort()
    
    return array_copy
