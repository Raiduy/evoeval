
from typing import List

def max_close_element_difference(numbers: List[float], threshold: float) -> float:
    max_diff = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                max_diff = max(max_diff, abs(numbers[i] - numbers[j]))
    return max_diff