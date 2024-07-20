

def derivative(xs: list):
    """
    This function computes the derivative of a polynomial represented by its coefficients.
    
    The input argument 'xs' is a list that contains the coefficients of a polynomial. Each element in the
    list corresponds to the coefficient of a polynomial term. The index of the coefficient in the list 
    determines the power of the term it is associated with. 

    In other words, the polynomial is represented as follows: xs[0] + xs[1] * x + xs[2] * x^2 + ....

    The function will return a list of coefficients that represents the derivative of this polynomial. The 
    derivative is represented in the same form as the input polynomial. 

    Here are a couple of examples to illustrate the functionality of this function.

    If the input is [3, 1, 2, 4, 5], the function will return [1, 4, 12, 20]. This is because the original 
    polynomial is 3 + x + 2x^2 + 4x^3 + 5x^4, and its derivative is 1 + 4x + 12x^2 + 20x^3

    If the input is [1, 2, 3], the function will return [2, 6]. This is because the original polynomial is 
    1 + 2x + 3x^2, and its derivative is 2 + 6x.

    Args:
    xs: A list of numbers representing the coefficients of a polynomial.

    Returns:
    A list of numbers representing the coefficients of the derivative of the input polynomial.
    """
    return [i * x for (i, x) in enumerate(xs)][1:]