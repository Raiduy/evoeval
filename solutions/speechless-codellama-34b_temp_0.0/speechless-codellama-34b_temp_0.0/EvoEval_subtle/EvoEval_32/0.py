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
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having at least two coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    if len(xs) < 2:
        raise ValueError('List must have at least two coefficients')
    if xs[-1] == 0:
        raise ValueError('Largest non-zero coefficient must be non-zero')
    x = 0
    while abs(poly(xs, x)) > 1e-06:
        x -= poly(xs, x) / poly(xs, 2 * x)
    return x