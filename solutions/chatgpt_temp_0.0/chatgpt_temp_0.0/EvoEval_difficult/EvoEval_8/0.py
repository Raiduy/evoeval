from typing import List, Tuple


def sum_product_odd_even(numbers: List[int]) -> Tuple[int, int, int, int]:
    odd_sum = 0
    odd_product = 1
    even_sum = 0
    even_product = 1
    for num in numbers:
        if abs(num) % 2 == 1:
            odd_sum += num
            odd_product *= num
        else:
            even_sum += num
            even_product *= num
    return (odd_sum, odd_product, even_sum, even_product)