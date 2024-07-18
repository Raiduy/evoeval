
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if abs(x) + abs(y) == z or abs(x) + abs(z) == y or abs(y) + abs(z) == x:
            return True
    return False