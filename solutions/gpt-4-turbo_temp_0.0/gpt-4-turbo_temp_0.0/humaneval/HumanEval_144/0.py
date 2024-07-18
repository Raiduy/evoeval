
def simplify(x, n):
    # Parse the fractions
    x_numerator, x_denominator = map(int, x.split('/'))
    n_numerator, n_denominator = map(int, n.split('/'))
    
    # Multiply the fractions
    result_numerator = x_numerator * n_numerator
    result_denominator = x_denominator * n_denominator
    
    # Check if the result is a whole number
    return result_numerator % result_denominator == 0
