
from typing import List
from fractions import Fraction

def filter_and_simplify(fractions: List[str], n: str) -> List[bool]:
    n = Fraction(n)
    result = []
    for fraction in fractions:
        fraction = Fraction(fraction)
        if (fraction * n).limit_denominator() == fraction * n:
            result.append(True)
        else:
            result.append(False)
    return result