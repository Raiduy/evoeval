
from typing import List, Tuple
import math


def closest_special_factorial(numbers: List[int]) -> Tuple[int, int]:
    """Find the two numbers with the closest special factorials."""
    special_factorials = {num: special_factorial(num) for num in numbers}
    sorted_numbers = sorted(numbers, key=lambda x: special_factorials[x])
    closest_pair = (0, 0)
    min_diff = float('inf')
    for i in range(len(sorted_numbers) - 1):
        diff = abs(special_factorials[sorted_numbers[i]] - special_factorials[sorted_numbers[i + 1]])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    return closest_pair