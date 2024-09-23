

def common(l1: list, l2: list):
    """
    This function, 'common', is designed to find and return the unique common elements between two lists. The lists are provided as input arguments, 'l1' and 'l2', and should be of type list. The function will iterate through both lists, finding all elements that appear in both. 

    It is important to note that the function will consider each unique common element only once, even if they appear more than once in the input lists. This means that the returned list will not have any duplicate values. 

    After all common elements have been found, the function will sort them in ascending order before returning. The sorting is performed to provide consistent output, and is done using the built-in sorting function in Python, which sorts in ascending (increasing) order by default.

    Here are some examples to demonstrate the function's behaviour:

    Example 1:
    Input: l1 = [1, 4, 3, 34, 653, 2, 5], l2 = [5, 7, 1, 5, 9, 653, 121]
    Output: [1, 5, 653]
    Explanation: The common elements are 1, 5 and 653. Sorted in ascending order, the output is [1, 5, 653].

    Example 2:
    Input: l1 = [5, 3, 2, 8], l2 = [3, 2]
    Output: [2, 3]
    Explanation: The common elements are 2 and 3. Sorted in ascending order, the output is [2, 3].
    
    """
    common_elements = set(l1) & set(l2)
    sorted_common_elements = sorted(list(common_elements))
    return sorted_common_elements