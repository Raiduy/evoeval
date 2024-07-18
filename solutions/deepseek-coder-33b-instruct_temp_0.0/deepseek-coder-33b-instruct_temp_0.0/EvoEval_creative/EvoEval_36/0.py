def calculate_integral_coefficients(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return indefinite integral of this polynomial in the same form, with the constant of integration set to zero,
    i.e. you should generate the coefficients for the polynomial representing the integral of the input polynomial.
    So for example, if the input is [3, 2, 1], then the output would represent the polynomial 3*x + x^2 + x^3/3
    >>> calculate_integral_coefficients([3, 2, 1])
    [0, 3.0, 1.0, 0.3333333333333333]
    >>> calculate_integral_coefficients([1, 3, 3, 1])
    [0, 1.0, 1.5, 1.0, 0.25]
    """
    integral_coefficients = [0]
    for i in range(len(xs)):
        integral_coefficients.append(xs[i] / (i + 1))
    return integral_coefficients