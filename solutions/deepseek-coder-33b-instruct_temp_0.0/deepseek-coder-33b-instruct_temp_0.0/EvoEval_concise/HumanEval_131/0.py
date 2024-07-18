
def digits(n):
    """Returns the product of the odd digits in a positive integer n, or 0 if all digits are even.

    Examples:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    has_odd = False
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
            has_odd = True
    if has_odd:
        return product
    else:
        return 0