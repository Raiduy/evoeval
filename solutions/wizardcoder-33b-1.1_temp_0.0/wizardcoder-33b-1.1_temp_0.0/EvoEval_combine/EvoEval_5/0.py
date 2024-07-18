
from typing import List

def sort_and_check(numbers: List[float], threshold: float) -> List[float]:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                first_and_last_sum = round(numbers[0] + numbers[-1])
                if first_and_last_sum % 2 == 0:
                    numbers.sort(reverse=True)
                else:
                    numbers.sort()
                return numbers
    return numbers