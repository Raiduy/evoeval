
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_num = 0
    product_num = 1
    for num in numbers:
        if num >= 0:
            sum_num += num
            product_num *= num
    return (sum_num, product_num)