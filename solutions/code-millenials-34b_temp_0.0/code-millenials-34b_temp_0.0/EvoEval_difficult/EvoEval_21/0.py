from typing import List, Optional

def rescale_to_unit(numbers: List[Optional[float]]) -> List[Optional[float]]:
    known_values = [x for x in numbers if x is not None]
    if not known_values:
        return numbers
    min_value = min(known_values)
    max_value = max(known_values)
    scaled_values = [(x - min_value) / (max_value - min_value) if x is not None else None for x in numbers]
    scaled_values = [round(x, 2) if x is not None else None for x in scaled_values]
    return scaled_values