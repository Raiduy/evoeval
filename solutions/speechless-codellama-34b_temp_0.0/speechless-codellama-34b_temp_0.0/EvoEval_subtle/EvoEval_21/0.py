
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)
    rescaled_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]
    return sorted(rescaled_numbers, reverse=True)