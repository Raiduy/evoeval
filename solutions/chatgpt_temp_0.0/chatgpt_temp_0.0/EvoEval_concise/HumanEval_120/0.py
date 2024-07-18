
def maximum(arr, k):
    """
    Given an array of integers 'arr' and a positive integer 'k', this function returns a sorted list of the top 'k' integers in 'arr'.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        - Array length: 1-1000.
        - Array elements: -1000 to 1000.
        - 'k' value: 0 to array length.
    """
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[:k]