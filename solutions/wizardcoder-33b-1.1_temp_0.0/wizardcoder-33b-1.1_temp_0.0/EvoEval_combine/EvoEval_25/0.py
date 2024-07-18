
from typing import List, Tuple

def sum_product_triples(n: int) -> Tuple[int, int]:
    a = [i * i - i + 1 for i in range(1, n + 1)]
    sum_of_first_elements = 0
    product_of_first_elements = 1
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    sum_of_first_elements += a[i]
                    product_of_first_elements *= a[i]
    return (sum_of_first_elements, product_of_first_elements)