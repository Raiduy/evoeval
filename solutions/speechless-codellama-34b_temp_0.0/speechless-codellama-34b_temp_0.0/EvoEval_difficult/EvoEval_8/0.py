from typing import List, Tuple


def sum_product_odd_even(numbers: List[int]) -> Tuple[int, int, int, int]:
    odd_sum = 0
    odd_product = 1
    even_sum = 0
    even_product = 1
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
            even_product *= num
        else:
            odd_sum += num
            odd_product *= num
    return (odd_sum, odd_product, even_sum, even_product)