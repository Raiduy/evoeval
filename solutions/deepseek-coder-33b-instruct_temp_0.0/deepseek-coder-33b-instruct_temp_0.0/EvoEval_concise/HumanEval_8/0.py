from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with the sum and product of a list of integers. For an empty list, sum is 0 and product is 1. 
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    else:
        sum_num = sum(numbers)
        product_num = 1
        for num in numbers:
            product_num *= num
        return (sum_num, product_num)