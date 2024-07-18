
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    rescaled_numbers = [(num - min_val) / range_val for num in numbers]
    return sorted(rescaled_numbers, reverse=True)