
def is_simple_power(x, n):
    """
    Check if x is a simple power of n and return the smallest power if true.
    """
    if n == 1:
        if x == 1:
            return (True, 0)
        else:
            return (False, None)
    power = 0
    while n ** power <= x:
        if n ** power == x:
            return (True, power)
        power += 1
    return (False, None)