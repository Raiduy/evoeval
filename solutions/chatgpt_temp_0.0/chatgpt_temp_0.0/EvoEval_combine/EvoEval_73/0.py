
from typing import List
from fractions import Fraction

def filter_and_simplify(fractions: List[str], n: str) -> List[bool]:
    result = []
    for fraction in fractions:
        fraction_obj = Fraction(fraction)
        n_obj = Fraction(n)
        multiplied_fraction = fraction_obj * n_obj
        result.append(multiplied_fraction.denominator == 1)
    return result