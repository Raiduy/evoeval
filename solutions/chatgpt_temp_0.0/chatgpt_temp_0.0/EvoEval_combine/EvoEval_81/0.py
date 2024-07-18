
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
    
    >>> mean_absolute_deviation_fibfib(1)
    0.0
    >>> mean_absolute_deviation_fibfib(5)
    0.64
    >>> mean_absolute_deviation_fibfib(8)
    3.375
    """

    def fibfib(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
    sequence = [fibfib(i) for i in range(n)]
    mean = sum(sequence) / n
    mad = sum((abs(x - mean) for x in sequence)) / n
    return round(mad, 2)