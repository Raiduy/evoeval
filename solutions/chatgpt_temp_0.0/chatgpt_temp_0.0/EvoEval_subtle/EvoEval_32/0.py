import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """xs are coefficients of a polynomial xs[0] + xs[1] * x^1 + xs[2] * x^3 + .... xs[n] * x^(2*n-1)
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having at least two coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-2, -3, 1]), 2) # (x + 1) (x + 1) (x - 2) = -2 - 3x + x^3
    -1.0
    """
    if len(xs) < 2:
        raise ValueError('List xs must have at least two coefficients.')
    n = len(xs) - 1
    largest_coeff = max(xs, key=abs)
    if largest_coeff == 0:
        raise ValueError('Largest non-zero coefficient must be non-zero.')
    if n % 2 == 0:
        raise ValueError('The polynomial must have an odd degree.')
    if n % 2 != 0:
        return -largest_coeff / xs[-2]