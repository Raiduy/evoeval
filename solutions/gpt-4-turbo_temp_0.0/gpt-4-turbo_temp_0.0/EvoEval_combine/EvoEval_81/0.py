
from typing import List

def mean_absolute_deviation_fibfib(n: int) -> float:
    """
    Given an integer n, calculate the mean absolute deviation of the first n elements of a modified Fibonacci sequence,
    called the FibFib sequence. The FibFib sequence is defined as follows:
    
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Then, compute the Mean Absolute Deviation (MAD) of these n elements. The MAD is the average absolute difference
    between each element and the mean of this set:
    MAD = average | x - x_mean |
    """
    if n == 0:
        return 0.0
    elif n == 1:
        return 0.0
    fibfib_sequence = [0, 0, 1] + [0] * (n - 3)
    for i in range(3, n):
        fibfib_sequence[i] = fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3]
    mean = sum(fibfib_sequence) / n
    mad = sum((abs(x - mean) for x in fibfib_sequence)) / n
    return mad