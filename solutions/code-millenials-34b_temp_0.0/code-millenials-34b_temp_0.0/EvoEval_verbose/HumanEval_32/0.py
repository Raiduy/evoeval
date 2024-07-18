
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
    
def find_zero(xs: list):
    """
    This function, find_zero, processes a list, xs, which contains the coefficients of a polynomial. The order of the coefficients
    should align with the degree of the terms of the polynomial, from the constant term to the highest degree term.

    The purpose of find_zero is to determine a value x such that when it is substituted into the polynomial, the result of the resulting calculation equals 0.
    This represents one of the roots of the polynomial expression, where the curve represented by the polynomial intersects the x-axis.

    Despite polynomials potentially having multiple roots (zero points), this function will return only one of them. This is due to its intended purpose,
    which is to quickly identify a single root rather than find all of them.

    For the function to guarantee a valid root or zero point, it only accepts input lists, xs, that contain an even number of coefficients. These coefficients
    should include a largest non-zero coefficient. As these features would assure the polynomial has at least one root.

    Thus, this function helps to find a root for polynomial functions in a simple and quick manner with certain assumptions about the polynomial's properties
    based on the input coefficient list.

    Examples:
    >>> round(find_zero([1, 2]), 2) # For the polynomial f(x) = 1 + 2x, one of the roots is x = -0.5
    -0.5

    >>> round(find_zero([-6, 11, -6, 1]), 2) # For the polynomial f(x) = -6 + 11x - 6x^2 + x^3 which expands to (x - 1) * (x - 2) * (x - 3), one of the roots is x = 1.0
    1.0
    """
    degree = len(xs) - 1
    x = 0
    while abs(poly(xs, x)) > 1e-06:
        derivative_at_x = sum([i * coeff * math.pow(x, i - 1) for (i, coeff) in enumerate(xs)])
        x -= poly(xs, x) / derivative_at_x
    return x