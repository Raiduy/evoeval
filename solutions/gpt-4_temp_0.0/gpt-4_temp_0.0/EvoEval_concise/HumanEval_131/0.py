
def digits(n):
    """Returns the product of the odd digits in a positive integer n, or 0 if all digits are even.

    Examples:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    has_odd = False
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
            has_odd = True
        n //= 10
    return product if has_odd else 0