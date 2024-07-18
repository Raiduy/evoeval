from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    This function takes a list of integers as input and returns a tuple as output. 
    The tuple contains two elements: the sum and the product of all the integers present in the input list.
    
    If the input list is empty, the function will return a tuple with both elements being default values.
    The default value for the sum (first element of the tuple) is 0, and the default value for the product (second element of the tuple) is 1. This is because the sum of an empty list is considered to be 0, and the product of an empty list is considered to be 1.
    
    The function is expected to handle lists of different lengths, including empty list. Each element in the list is expected to be an integer. The order of integers in the list does not influence the output.
    
    Here are some examples of how this function can be used:

    Example 1:
    Input: []
    Output: (0, 1)
    Explanation: The input list is empty, so the function returns the default sum (0) and product (1).
    
    Example 2:
    Input: [1, 2, 3, 4]
    Output: (10, 24)
    Explanation: The input list contains four integers. The sum of these integers is 1 + 2 + 3 + 4 = 10. The product of these integers is 1 * 2 * 3 * 4 = 24.
    """
    if not numbers:
        return (0, 1)
    sum_result = sum(numbers)
    product_result = 1
    for num in numbers:
        product_result *= num
    return (sum_result, product_result)