from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each number and the mean
    absolute_differences = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute differences
    mad = sum(absolute_differences) / len(absolute_differences)

    return mad
