
def is_simple_power(x, n):
    """
    Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases. Additionally, return the smallest power that makes x a simple power of n.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => (true, 0)
    is_simple_power(2, 2) => (true, 1)
    is_simple_power(8, 2) => (true, 3)
    is_simple_power(3, 2) => (false, None)
    is_simple_power(3, 1) => (false, None)
    is_simple_power(5, 3) => (false, None)
    """
    if x == 1:
        return (True, 0)
    power = 1
    while n ** power < x:
        power += 1
    if n ** power == x:
        return (True, power)
    else:
        return (False, None)