
def simplify(x, n):
    # Convert the fractions to integers
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    # Calculate the product of the fractions
    product_num = x_num * n_num
    product_den = x_den * n_den

    # Check if the product is a whole number
    if product_num % product_den == 0:
        return True
    else:
        return False
