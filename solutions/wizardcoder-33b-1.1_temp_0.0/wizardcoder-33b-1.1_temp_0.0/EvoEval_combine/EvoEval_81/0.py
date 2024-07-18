
from typing import List

def mean_absolute_deviation_fibfib(n: int) -> float:
    fibfib = [0, 0, 1]
    for i in range(3, n):
        fibfib.append(fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3])
    mean = sum(fibfib) / n
    mad = sum((abs(x - mean) for x in fibfib)) / n
    return round(mad, 2)