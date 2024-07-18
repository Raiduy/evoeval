from typing import List, Tuple

def has_close_elements_in_range(numbers: List[Tuple[float, float]], threshold: float) -> bool:
    numbers.sort(key=lambda x: x[0])
    for i in range(len(numbers) - 1):
        first_diff = numbers[i + 1][0] - numbers[i][0]
        second_diff = numbers[i + 1][1] - numbers[i][1]
        if first_diff < threshold and second_diff < threshold:
            return True
    return False