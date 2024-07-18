
def is_simple_power(x, n):
    """
    Returns True if a number x is a simple power of n and False in other cases.
    """
    if x == n:
        return True
    elif x < n:
        return False
    else:
        i = 1
        while x >= n:
            x = x / n
            if x == 1:
                return True
            elif x < n:
                return False
            i += 1
        return False
