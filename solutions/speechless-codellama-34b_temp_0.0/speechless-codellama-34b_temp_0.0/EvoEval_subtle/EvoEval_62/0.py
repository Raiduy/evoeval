

def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form, but in descending order of the power of x.
    """
    derivative_coefficients = []
    for i in range(len(xs) - 1, 0, -1):
        derivative_coefficients.append(xs[i] * i)
    return derivative_coefficients