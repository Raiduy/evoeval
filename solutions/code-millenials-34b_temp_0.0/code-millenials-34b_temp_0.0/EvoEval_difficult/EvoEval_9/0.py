from typing import List, Tuple

def rolling_max_min(numbers: List[int]) -> List[Tuple[int, int]]:
    if not numbers:
        return []
    max_val = numbers[0]
    min_val = numbers[0]
    result = [(numbers[0], numbers[0])]
    for num in numbers[1:]:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        result.append((max_val, min_val))
    return result