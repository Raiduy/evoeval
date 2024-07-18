from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with the sum and product of a list of integers. For an empty list, sum is 0 and product is 1. 
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_of_numbers = 0
    product_of_numbers = 1
    for number in numbers:
        sum_of_numbers += number
        product_of_numbers *= number
    return (sum_of_numbers, product_of_numbers)