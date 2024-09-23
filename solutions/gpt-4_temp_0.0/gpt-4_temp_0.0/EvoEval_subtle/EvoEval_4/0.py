
from typing import List


def median_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Deviation
    around the median of this dataset.
    Median Absolute Deviation is the median absolute difference between each
    element and a centerpoint (median in this case):
    MAD = median | x - x_median |
    >>> median_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    median = np.median(numbers)
    deviations = [abs(x - median) for x in numbers]
    mad = np.median(deviations)
    return mad