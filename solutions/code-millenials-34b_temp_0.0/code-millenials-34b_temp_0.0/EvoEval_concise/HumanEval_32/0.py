
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ Takes a list xs of even number of coefficients for a polynomial, where the largest coefficient is non zero. Returns a zero value of the polynomial.
    Note: Only returns one zero point even when multiple exist.

    >>> round(find_zero([1, 2]), 2)
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2)
    1.0
    """
    x = 0
    while abs(poly(xs, x)) > 1e-06:
        deriv = [i * coeff for (i, coeff) in enumerate(xs)][1:]
        deriv_x = poly(deriv, x)
        x = x - poly(xs, x) / deriv_x
    return x