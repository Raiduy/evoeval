
from typing import List, Tuple
import math


def closest_special_factorial(numbers: List[int]) -> Tuple[int, int]:

    def special_factorial(n: int) -> int:
        result = 1
        for i in range(1, n + 1):
            result *= math.factorial(i)
        return result
    closest_pair = None
    min_difference = float('inf')
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            difference = abs(special_factorial(numbers[i]) - special_factorial(numbers[j]))
            if difference < min_difference:
                min_difference = difference
                closest_pair = (numbers[i], numbers[j])
    return tuple(sorted(closest_pair))