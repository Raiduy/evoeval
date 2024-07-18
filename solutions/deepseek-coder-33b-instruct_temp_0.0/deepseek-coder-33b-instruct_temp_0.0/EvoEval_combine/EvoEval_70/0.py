
from typing import List, Tuple
import math


def closest_special_factorial(numbers: List[int]) -> Tuple[int, int]:

    def special_factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * special_factorial(n - 1)
    numbers.sort()
    min_diff = float('inf')
    result = (0, 0)
    for i in range(1, len(numbers)):
        diff = abs(special_factorial(numbers[i]) - special_factorial(numbers[i - 1]))
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i - 1], numbers[i])
    return result