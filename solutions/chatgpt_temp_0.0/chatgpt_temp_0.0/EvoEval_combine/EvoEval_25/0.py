
from typing import List, Tuple

def sum_product_triples(n: int) -> Tuple[int, int]:
    a = [i * i - i + 1 for i in range(1, n + 1)]
    triples = [(a[i], a[j], a[k]) for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n) if (a[i] + a[j] + a[k]) % 3 == 0]
    if not triples:
        return (0, 1)
    sum_first_elements = sum((triple[0] for triple in triples))
    product_first_elements = 1
    for triple in triples:
        product_first_elements *= triple[0]
    return (sum_first_elements, product_first_elements)