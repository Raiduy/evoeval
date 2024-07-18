def simplify(x, n):
    """Implements a function that checks if the multiplication of two fractions results in a whole number.
    
    Both fractions x and n are represented as strings in the format '<numerator>/<denominator>'. 
    The numerator and denominator are positive integers. 
    
    Returns True if the multiplication results in a whole number, False otherwise.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    (x_num, x_den) = map(int, x.split('/'))
    (n_num, n_den) = map(int, n.split('/'))
    new_num = x_num * n_num
    new_den = x_den * n_den
    if new_den % new_num == 0:
        return True
    else:
        return False