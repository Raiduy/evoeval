from typing import List, Tuple


def sum_product_odd_even(numbers: List[int]) -> Tuple[int, int, int, int]:
    sum_odd = 0
    product_odd = 1
    sum_even = 0
    product_even = 1
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
            product_even *= num
        else:
            sum_odd += num
            product_odd *= num
    return (sum_odd, product_odd, sum_even, product_even)