
def pluck(arr):
    """
    Given an array (representing a tree branch with non-negative integer nodes), 
    this function returns a list of the smallest even node value and its index. 
    If multiple nodes have the same smallest even value, the one with the smallest index is returned. 
    If no even values exist or the array is empty, an empty list is returned.

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]

    Note:
        * Array length: 1 <= nodes.length <= 10000
        * Node values: 0 <= node.value
    """
    smallest_even = float('inf')
    smallest_even_index = -1
    for (i, num) in enumerate(arr):
        if num % 2 == 0 and num < smallest_even:
            smallest_even = num
            smallest_even_index = i
    if smallest_even_index == -1:
        return []
    else:
        return [smallest_even, smallest_even_index]