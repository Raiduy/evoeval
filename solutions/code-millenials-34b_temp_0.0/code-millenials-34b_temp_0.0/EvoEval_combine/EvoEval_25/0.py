
from typing import List, Tuple

def sum_product_triples(n: int) -> Tuple[int, int]:
    a = [i * i - i + 1 for i in range(1, n + 1)]
    triple_sum = 0
    triple_product = 1
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    triple_sum += a[i]
                    triple_product *= a[i]
    return (triple_sum, triple_product)