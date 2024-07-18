
from typing import List, Tuple

def sum_product_triples(n: int) -> Tuple[int, int]:
    a = [i * i - i + 1 for i in range(1, n + 1)]
    valid_triples = [(a[i], a[j], a[k]) for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n) if (a[i] + a[j] + a[k]) % 3 == 0]
    if not valid_triples:
        return (0, 1)
    else:
        return (sum((triple[0] for triple in valid_triples)), eval('*'.join((str(triple[0]) for triple in valid_triples))))