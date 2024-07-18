from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = None
    smallest_diff = None
    for i in range(len(numbers) - 1):
        pair = (numbers[i], numbers[i + 1])
        diff = pair[1] - pair[0]
        if smallest_diff is None or diff < smallest_diff:
            closest_pair = pair
            smallest_diff = diff
    return (closest_pair[1], closest_pair[0])