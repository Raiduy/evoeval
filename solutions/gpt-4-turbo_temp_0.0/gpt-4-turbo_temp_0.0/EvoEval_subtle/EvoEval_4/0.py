
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
    if not numbers:
        return 0.0

    def median(lst: List[float]) -> float:
        sorted_lst = sorted(lst)
        lst_len = len(lst)
        index = (lst_len - 1) // 2
        if lst_len % 2:
            return sorted_lst[index]
        else:
            return (sorted_lst[index] + sorted_lst[index + 1]) / 2.0
    med = median(numbers)
    abs_diff = [abs(x - med) for x in numbers]
    mad = median(abs_diff)
    return mad