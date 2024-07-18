
from typing import List

def sort_and_check(numbers: List[float], threshold: float) -> List[float]:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                if round(sum(numbers[:2])) % 2 == 0:
                    return sorted(numbers, reverse=True)
                else:
                    return sorted(numbers)
    return numbers