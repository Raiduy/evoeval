from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    This function aims to remove all duplicated elements from a list of integers. It does this by iterating 
    through the input list and removing any repeated elements that it encounters. The unique feature of this 
    function is that it preserves the original order of the elements in the list. This means that the elements 
    in the returned list will appear in the same order as they did in the input list.

    The function takes one argument:
    1. numbers (List[int]) : A list of integers from which duplicates need to be removed. 

    The function returns a list of integers (List[int]) where all the duplicated elements have been removed and 
    the order of the elements is the same as the original list.

    An example to illustrate the usage of the function:

    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]

    In this example, the function is given a list of integers [1, 2, 3, 2, 4]. The function removes the duplicate 
    element '2' from the list and returns a new list with the remaining elements in their original order.
    """
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers