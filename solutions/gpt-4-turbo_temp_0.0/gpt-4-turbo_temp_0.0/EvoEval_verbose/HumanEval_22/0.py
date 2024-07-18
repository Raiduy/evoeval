from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ 
    This function filters a given list of any type of Python values and returns a list of integers only. 

    The input to the function is a list that can contain any type of Python values such as numbers, strings, dictionaries, lists, etc. The function will go through each element in the list and keep only those that are integers. The output will be a new list with the integers from the input list. Any non-integer values in the input list will be discarded. 

    If the input list is empty, the function will return an empty list. If the input list contains no integer values, the function will also return an empty list. 

    Parameters:
    values (List[Any]): A list of any Python values

    Returns:
    List[int]: A list containing only integers from the input list

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]

    Note: The function does not modify the original list, it returns a new list.
    """
    return [value for value in values if isinstance(value, int)]