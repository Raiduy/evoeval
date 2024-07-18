
def digits(n):
    """
    This function calculates and returns the total product of all the odd digits in the input integer n.
    """
    n_str = str(n)
    product = 1
    has_odd = False
    for char in n_str:
        digit = int(char)
        if digit % 2 != 0:
            product *= digit
            has_odd = True
    if not has_odd:
        return 0
    else:
        return product