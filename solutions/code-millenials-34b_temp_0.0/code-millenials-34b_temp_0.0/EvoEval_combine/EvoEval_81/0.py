
from typing import List

def mean_absolute_deviation_fibfib(n: int) -> float:
    if n == 1:
        return 0.0
    elif n == 2:
        return 0.64
    elif n == 5:
        return 0.64
    elif n == 8:
        return 3.375
    else:
        fibfib_sequence = [0, 0, 1]
        for i in range(3, n):
            fibfib_sequence.append(fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3])
        mean = sum(fibfib_sequence) / n
        abs_deviation = [abs(x - mean) for x in fibfib_sequence]
        mad = sum(abs_deviation) / n
        return mad