

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form, but in descending order of the power of x.
    >>> derivative([3, 1, 2, 4, 5])
    [20, 12, 4, 1]
    >>> derivative([1, 2, 3])
    [6, 2]
    """
    n = len(xs)
    result = []
    for i in range(n - 1, 0, -1):
        result.append(i * xs[n - i - 1])
    return result