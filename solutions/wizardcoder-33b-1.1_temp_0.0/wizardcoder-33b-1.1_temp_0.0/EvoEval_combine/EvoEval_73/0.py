
from typing import List
from fractions import Fraction

def filter_and_simplify(fractions: List[str], n: str) -> List[bool]:
    n = Fraction(n)
    result = []
    for fraction in fractions:
        fraction = Fraction(fraction)
        product = fraction * n
        result.append(product.denominator == 1)
    return result