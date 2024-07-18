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
        total_sum = sum(numbers)
        total_product = 1
        for num in numbers:
            total_product *= num
        return (total_sum, total_product)