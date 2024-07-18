from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[0] - numbers[1])
    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    return closest_pair if closest_pair[0] > closest_pair[1] else (closest_pair[1], closest_pair[0])