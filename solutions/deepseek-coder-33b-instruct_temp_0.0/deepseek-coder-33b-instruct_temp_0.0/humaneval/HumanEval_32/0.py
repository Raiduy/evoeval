import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check if the list has an even number of coefficients
    if len(xs) % 2 == 0:
        raise ValueError("The list of coefficients must have an odd number of elements.")

    # Find the largest non-zero coefficient
    max_coeff = max(xs)

    # If the largest coefficient is 0, raise an error
    if max_coeff == 0:
        raise ValueError("The largest coefficient must be non-zero.")

    # Calculate the zero point
    zero_point = -xs[-2] / xs[-1]

    return zero_point
