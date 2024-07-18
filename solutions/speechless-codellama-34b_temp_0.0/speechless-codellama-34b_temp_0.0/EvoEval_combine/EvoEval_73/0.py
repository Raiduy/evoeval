
from typing import List
from fractions import Fraction

def filter_and_simplify(fractions: List[str], n: str) -> List[bool]:
    n_fraction = Fraction(n)
    result = []
    for fraction in fractions:
        frac = Fraction(fraction)
        if frac * n_fraction == frac.numerator:
            result.append(True)
        else:
            result.append(False)
    return result