

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of x^n is n*x^(n-1)
    # So, we just multiply each coefficient by its index (which is the power)
    # and return the list of these products
    return [i * xs[i] for i in range(1, len(xs))]
