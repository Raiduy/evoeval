
def is_simple_power(x, n):
    if n == 1:
        return (False, None)
    power = 0
    while n ** power < x:
        power += 1
    if n ** power == x:
        return (True, power)
    else:
        return (False, None)