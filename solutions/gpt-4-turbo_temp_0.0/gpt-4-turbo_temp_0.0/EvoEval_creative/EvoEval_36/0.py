def calculate_integral_coefficients(xs: list):
    """
    Calculate the coefficients of the indefinite integral of a polynomial.
    
    Args:
    xs (list): Coefficients of the polynomial, where xs[i] is the coefficient for x^i.
    
    Returns:
    list: Coefficients of the indefinite integral of the polynomial, with the constant of integration set to zero.
    """
    integral_coefficients = [0]
    for (i, coeff) in enumerate(xs):
        integral_coefficients.append(coeff / (i + 1))
    return integral_coefficients