from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ Calculate the Mean Absolute Deviation (MAD) of the list.
    MAD is the average absolute deviation from the mean:
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = sum(numbers) / len(numbers)
    deviations = [abs(x - mean) for x in numbers]
    mad = sum(deviations) / len(deviations)
    return mad