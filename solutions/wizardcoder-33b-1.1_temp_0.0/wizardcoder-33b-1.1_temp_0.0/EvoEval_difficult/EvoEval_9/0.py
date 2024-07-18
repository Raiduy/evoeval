from typing import List, Tuple

def rolling_max_min(numbers: List[int]) -> List[Tuple[int, int]]:
    if not numbers:
        return []
    rolling_max = numbers[0]
    rolling_min = numbers[0]
    result = [(rolling_max, rolling_min)]
    for num in numbers[1:]:
        if num > rolling_max:
            rolling_max = num
        if num < rolling_min:
            rolling_min = num
        result.append((rolling_max, rolling_min))
    return result