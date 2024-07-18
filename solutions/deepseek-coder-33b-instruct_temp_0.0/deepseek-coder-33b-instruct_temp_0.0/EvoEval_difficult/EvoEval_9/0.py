from typing import List, Tuple

def rolling_max_min(numbers: List[int]) -> List[Tuple[int, int]]:
    if not numbers:
        return []
    result = [(numbers[0], numbers[0])]
    current_max = numbers[0]
    current_min = numbers[0]
    for num in numbers[1:]:
        current_max = max(current_max, num)
        current_min = min(current_min, num)
        result.append((current_max, current_min))
    return result