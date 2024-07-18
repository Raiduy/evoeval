from typing import List, Tuple

def rolling_max_min(numbers: List[int]) -> List[Tuple[int, int]]:
    if not numbers:
        return []
    max_num = numbers[0]
    min_num = numbers[0]
    result = [(max_num, min_num)]
    for num in numbers[1:]:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        result.append((max_num, min_num))
    return result