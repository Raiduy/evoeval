
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
    
def find_zero(xs: list) -> float:
    """
    Finds a zero of the polynomial with coefficients xs using the Newton-Raphson method.
    """
    if len(xs) % 2 == 0:
        x0 = 0.0
        dxs = poly_derivative(xs)
        for _ in range(100):
            try:
                x1 = x0 - poly(xs, x0) / poly(dxs, x0)
                if abs(x1 - x0) < 1e-06:
                    return x1
                x0 = x1
            except ZeroDivisionError:
                x0 += 1.0
        raise ValueError('Failed to converge to a root')
    else:
        raise ValueError('Input list must contain an even number of coefficients')