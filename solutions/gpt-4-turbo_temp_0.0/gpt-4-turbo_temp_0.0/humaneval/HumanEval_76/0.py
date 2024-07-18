
def is_simple_power(x, n):
    # Edge case: n == 1, only 1**0 = 1 is true, any other x would be false
    if n == 1:
        return x == 1
    
    # Start with m = 0 and increase it until n**m is greater than or equal to x
    m = 0
    while n ** m < x:
        m += 1
    
    # Check if n**m equals x
    return n ** m == x
