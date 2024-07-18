

def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    """
    return [i*x for i, x in enumerate(xs)][1:]
