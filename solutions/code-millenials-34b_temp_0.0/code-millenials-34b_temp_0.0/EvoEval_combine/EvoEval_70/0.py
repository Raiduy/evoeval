
from typing import List, Tuple
import math


def closest_special_factorial(numbers: List[int]) -> Tuple[int, int]:
    special_fact = [special_factorial(n) for n in numbers]
    min_diff = float('inf')
    result = (0, 0)
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(special_fact[i] - special_fact[j]) < min_diff:
                min_diff = abs(special_fact[i] - special_fact[j])
                result = (numbers[i], numbers[j]) if numbers[i] < numbers[j] else (numbers[j], numbers[i])
    return result