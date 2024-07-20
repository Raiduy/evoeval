def derivative(xs: list, x: float) -> float:
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial at the given value of x
    """
    derivative_value = 0
    for i in range(1, len(xs)):
        derivative_value += i * xs[i] * x ** (i - 1)
    return derivative_value