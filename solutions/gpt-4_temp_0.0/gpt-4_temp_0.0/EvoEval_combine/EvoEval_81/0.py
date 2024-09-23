
from typing import List

def mean_absolute_deviation_fibfib(n: int) -> float:

    def fibfib(n: int) -> int:
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
    fibfib_sequence = [fibfib(i) for i in range(n)]
    mean = sum(fibfib_sequence) / n
    mad = sum((abs(x - mean) for x in fibfib_sequence)) / n
    return mad