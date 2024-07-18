

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form, but in descending order of the power of x.
    >>> derivative([3, 1, 2, 4, 5])
    [20, 12, 4, 1]
    >>> derivative([1, 2, 3])
    [6, 2]
    """
    derivative_coefficients = [0]
    for i in range(1, len(xs)):
        derivative_coefficients.append(i * xs[i])
    return derivative_coefficients