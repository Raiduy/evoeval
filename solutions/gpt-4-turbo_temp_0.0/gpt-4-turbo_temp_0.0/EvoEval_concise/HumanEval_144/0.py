def simplify(x, n):
    """Implements a function that checks if the multiplication of two fractions results in a whole number.
    
    Both fractions x and n are represented as strings in the format '<numerator>/<denominator>'. 
    The numerator and denominator are positive integers. 
    
    Returns True if the multiplication results in a whole number, False otherwise.
    """
    (num1, den1) = map(int, x.split('/'))
    (num2, den2) = map(int, n.split('/'))
    result_num = num1 * num2
    result_den = den1 * den2
    return result_num % result_den == 0