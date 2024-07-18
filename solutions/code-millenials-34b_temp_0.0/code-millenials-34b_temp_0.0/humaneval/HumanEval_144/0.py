
def simplify(x, n):
    # Split the fractions into numerator and denominator
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    # Calculate the product of the numerators and the product of the denominators
    prod_num = x_num * n_num
    prod_den = x_den * n_den
    
    # Check if the result is a whole number
    return prod_num % prod_den == 0
