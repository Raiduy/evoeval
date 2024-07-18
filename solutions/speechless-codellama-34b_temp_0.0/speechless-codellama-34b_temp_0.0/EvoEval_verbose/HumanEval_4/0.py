from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    differences = [abs(number - mean) for number in numbers]
    mad = sum(differences) / len(differences)
    return mad