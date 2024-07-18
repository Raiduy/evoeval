
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

    def derivative(xs: list, x: float):
        return sum([i * coeff * math.pow(x, i - 1) for (i, coeff) in enumerate(xs) if i != 0])
    x_n = xs[-1]
    while True:
        fx_n = poly(xs, x_n)
        if abs(fx_n) < 1e-05:
            return x_n
        dfx_n = derivative(xs, x_n)
        if dfx_n == 0:
            print('Zero derivative. No solution found.')
            return None
        x_n = x_n - fx_n / dfx_n