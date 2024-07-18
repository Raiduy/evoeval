
from typing import List, Tuple


def rolling_min(numbers: List[int]) -> List[int]:
    min_val = float('inf')
    result = []
    for num in numbers:
        min_val = min(min_val, num)
        result.append(min_val)
    return result