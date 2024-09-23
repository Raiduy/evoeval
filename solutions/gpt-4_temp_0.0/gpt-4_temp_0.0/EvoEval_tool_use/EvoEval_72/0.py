def check_divisibility(n1, n2):
    '''
    Helper function to check if the first number (n1) is divisible by the second number (n2).
    Returns True if n1 is divisible by n2, False otherwise.
    '''
    if n1 % n2 == 0:
        return True
    else:
        return False
def is_strong(n):
    """
    Write a function that returns True if the number n is strong, and False otherwise.
    A number is considered strong if it is divisible by every digit in the number.
    """
    for digit in str(n):
        if not check_divisibility(n, int(digit)):
            return False
    return True