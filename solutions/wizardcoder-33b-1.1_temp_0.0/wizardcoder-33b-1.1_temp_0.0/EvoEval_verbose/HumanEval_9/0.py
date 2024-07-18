from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = []
    for i in range(len(numbers)):
        if i == 0:
            max_numbers.append(numbers[i])
        else:
            max_numbers.append(max(max_numbers[i - 1], numbers[i]))
    return max_numbers