from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ Calculate the Mean Absolute Deviation (MAD) of the list.
    MAD is the average absolute deviation from the mean:
    MAD = average | x - x_mean |
    """
    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(num - mean) for num in numbers]
    mad = sum(absolute_deviations) / len(absolute_deviations)
    return mad