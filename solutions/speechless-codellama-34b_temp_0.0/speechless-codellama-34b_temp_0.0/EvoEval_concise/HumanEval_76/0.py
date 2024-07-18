
def is_simple_power(x, n):
    i = 0
    while n ** i <= x:
        if n ** i == x:
            return True
        i += 1
    return False