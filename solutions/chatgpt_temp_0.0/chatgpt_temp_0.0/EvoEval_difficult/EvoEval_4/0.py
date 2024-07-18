from typing import List, Tuple


def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    total_weight = sum((w for (_, w) in numbers))
    if total_weight != 1 or any((w <= 0 for (_, w) in numbers)):
        return 'Weights must be positive and sum to 1'
    weighted_mean = sum((x * w for (x, w) in numbers)) / total_weight
    wmad = sum((w * abs(x - weighted_mean) for (x, w) in numbers)) / total_weight
    return wmad