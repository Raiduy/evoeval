
from typing import List, Tuple


def rolling_min(numbers: List[int]) -> List[int]:
    result = []
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
        result.append(min_value)
    return result