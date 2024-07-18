
def is_simple_power(x, n):
    if n == 1:
        return x == 1
    else:
        i = 0
        while n ** i < x:
            i += 1
        return n ** i == x