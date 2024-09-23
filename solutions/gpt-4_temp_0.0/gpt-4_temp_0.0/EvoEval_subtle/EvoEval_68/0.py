
def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest odd value.
    If multiple nodes with the same smallest odd value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ its index, smalest_value ],
    If there are no odd values or the given array is empty, return [].

    Example 1:
        Input: [4,3,5]
        Output: [1, 3]
        Explanation: 3 has the smallest odd value, and 3 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [0, 1]
        Explanation: 1 has the smallest odd value, and 1 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 1, 3, 0, 4, 2]
        Output: [1, 1]
        Explanation: 1 is the smallest value, but  there are two ones,
                     so we will choose the first one, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    odd_values = [(i, v) for (i, v) in enumerate(arr) if v % 2 != 0]
    if not odd_values:
        return []
    return min(odd_values, key=lambda x: x[1])