from typing import List, Tuple


def weighted_mean_absolute_deviation(numbers: List[Tuple[float, float]]) -> float:
    weights_sum = sum((weight for (_, weight) in numbers))
    if any((weight < 0 for (_, weight) in numbers)) or weights_sum != 1:
        return 'Weights must be positive and sum to 1'
    weighted_mean = sum((x * weight for (x, weight) in numbers))
    wmad = sum((weight * abs(x - weighted_mean) for (x, weight) in numbers)) / weights_sum
    return wmad