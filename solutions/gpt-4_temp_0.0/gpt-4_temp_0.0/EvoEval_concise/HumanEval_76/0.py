
def is_simple_power(x, n):
    """Returns true if x is an integer power of n, false otherwise.
    
    A number x is an integer power of n if there exists some integer i such that n**i = x
    
    Examples:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if x == 1:
        return True
    elif n == 1:
        return x == 1
    else:
        i = 0
        while n ** i <= x:
            if n ** i == x:
                return True
            i += 1
        return False