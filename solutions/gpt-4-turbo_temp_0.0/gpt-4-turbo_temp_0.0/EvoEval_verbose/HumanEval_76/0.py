
def is_simple_power(x, n):
    if n == 1:
        return x == 1
    i = 0
    while True:
        power = n ** i
        if power == x:
            return True
        elif power > x:
            return False
        i += 1