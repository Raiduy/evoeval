
from typing import List
from fractions import Fraction

def filter_and_simplify(fractions: List[str], n: str) -> List[bool]:
    """ Filter an input list of fractions only for ones that, when multiplied by n, simplify to a whole number. Both, fractions in the list and n, are string representation of a fraction, and have the following format, <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that the fractions, and n are valid fractions, and do not have zero as denominator.

    filter_and_simplify(["1/5", "1/6", "7/10"], "5/1") = [True, False, False]
    filter_and_simplify(["1/3", "2/1", "3/2"], "2/1") = [False, True, True]
    """
    n_fraction = Fraction(n)
    result = []
    for fraction in fractions:
        product = Fraction(fraction) * n_fraction
        result.append(product.denominator == 1)
    return result