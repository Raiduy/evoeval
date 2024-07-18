
def is_simple_power(x, n):
    if x == 1:
        return (True, 0)
    power = 1
    while n ** power < x:
        power += 1
    if n ** power == x:
        return (True, power)
    else:
        return (False, None)