from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    sorted_numbers = sorted(numbers)
    for i in range(len(sorted_numbers) - 1):
        difference = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        if difference < threshold:
            return True
    return False