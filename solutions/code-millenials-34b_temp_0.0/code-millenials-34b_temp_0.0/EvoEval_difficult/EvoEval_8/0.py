from typing import List, Tuple


def sum_product_odd_even(numbers: List[int]) -> Tuple[int, int, int, int]:
    sum_odd = 0
    product_odd = 1
    sum_even = 0
    product_even = 1
    for num in numbers:
        abs_num = abs(num)
        if abs_num % 2 == 0:
            sum_even += abs_num
            product_even *= abs_num
        else:
            sum_odd += abs_num
            product_odd *= abs_num
    return (sum_odd, product_odd, sum_even, product_even)