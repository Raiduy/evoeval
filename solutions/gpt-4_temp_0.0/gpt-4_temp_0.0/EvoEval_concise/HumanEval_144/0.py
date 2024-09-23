def simplify(x, n):
    """Implements a function that checks if the multiplication of two fractions results in a whole number.
    
    Both fractions x and n are represented as strings in the format '<numerator>/<denominator>'. 
    The numerator and denominator are positive integers. 
    
    Returns True if the multiplication results in a whole number, False otherwise.
    """
    (x_num, x_den) = map(int, x.split('/'))
    (n_num, n_den) = map(int, n.split('/'))
    result_num = x_num * n_num
    result_den = x_den * n_den
    return result_num % result_den == 0