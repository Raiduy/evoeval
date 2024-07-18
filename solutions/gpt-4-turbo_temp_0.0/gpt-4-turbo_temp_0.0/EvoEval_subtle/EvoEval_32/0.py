import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Uses Newton's method to find a zero of the polynomial defined by xs.
    """
    x0 = 0.0
    tolerance = 1e-06
    max_iterations = 1000
    for _ in range(max_iterations):
        fx = poly(xs, x0)
        dfx = poly_derivative(xs, x0)
        if abs(dfx) < tolerance:
            raise ValueError("Derivative too small; Newton's method fails.")
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tolerance:
            return x1
        x0 = x1
    raise ValueError("Newton's method did not converge.")