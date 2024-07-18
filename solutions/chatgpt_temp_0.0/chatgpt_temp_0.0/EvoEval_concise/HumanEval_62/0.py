

def derivative(xs: list):
    """ 
    Returns the derivative of a polynomial represented by list 'xs', where each element corresponds to a coefficient. 
    The list index represents the power of x (i.e., xs[i]*x^i).
    
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    derivative_xs = []
    for i in range(1, len(xs)):
        derivative_xs.append(i * xs[i])
    return derivative_xs