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

    Example:
    is_strong(128) ➞ True 
    # 128 is divisible by 1, 2, and 8.

    is_strong(12) ➞ True 
    # 12 is divisible by 1 and 2.

    is_strong(111) ➞ True
    # 111 is divisible by 1.

    is_strong(10) ➞ False
    # 10 is not divisible by 0 (division by zero is undefined).
    """
    digits = [int(d) for d in str(n)]
    for digit in digits:
        if digit == 0:
            return False
        if not check_divisibility(n, digit):
            return False
    return True