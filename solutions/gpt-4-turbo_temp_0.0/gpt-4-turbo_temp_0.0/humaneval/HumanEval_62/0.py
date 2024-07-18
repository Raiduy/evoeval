

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of a constant is 0, so we skip the first coefficient (xs[0]).
    # We start with the coefficient of x (xs[1]), which is simply multiplied by its index (1 in this case).
    # For each coefficient, we multiply it by its index (which represents the power of x) to get the derivative.
    return [i * xs[i] for i in range(1, len(xs))]
