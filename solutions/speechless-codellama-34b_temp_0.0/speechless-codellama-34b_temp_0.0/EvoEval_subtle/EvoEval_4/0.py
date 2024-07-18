
from typing import List


def median_absolute_deviation(numbers: List[float]) -> float:
    median = statistics.median(numbers)
    diffs = [abs(x - median) for x in numbers]
    mad = statistics.median(diffs)
    return mad