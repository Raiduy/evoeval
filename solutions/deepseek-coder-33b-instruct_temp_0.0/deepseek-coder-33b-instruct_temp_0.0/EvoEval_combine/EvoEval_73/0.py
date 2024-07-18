
from typing import List
from fractions import Fraction

def filter_and_simplify(fractions: List[str], n: str) -> List[bool]:
    n_fraction = Fraction(n)
    result = []
    for fraction in fractions:
        fraction_obj = Fraction(fraction)
        product = fraction_obj * n_fraction
        result.append(product.denominator == 1)
    return result