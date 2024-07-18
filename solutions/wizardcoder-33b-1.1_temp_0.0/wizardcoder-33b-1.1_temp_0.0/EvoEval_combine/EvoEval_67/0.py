
from typing import List

def max_close_element_difference(numbers: List[float], threshold: float) -> float:
    numbers.sort()
    max_diff = 0
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if diff < threshold and diff > max_diff:
            max_diff = diff
    return max_diff