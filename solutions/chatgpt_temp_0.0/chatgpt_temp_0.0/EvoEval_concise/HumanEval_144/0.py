def simplify(x, n):
    """Implements a function that checks if the multiplication of two fractions results in a whole number.
    
    Both fractions x and n are represented as strings in the format '<numerator>/<denominator>'. 
    The numerator and denominator are positive integers. 
    
    Returns True if the multiplication results in a whole number, False otherwise.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    (x_num, x_denom) = map(int, x.split('/'))
    (n_num, n_denom) = map(int, n.split('/'))
    result_num = x_num * n_num
    result_denom = x_denom * n_denom
    return result_num % result_denom == 0