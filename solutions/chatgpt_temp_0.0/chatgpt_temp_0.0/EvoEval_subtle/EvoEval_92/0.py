
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x == abs(y) + abs(z) or y == abs(x) + abs(z) or z == abs(x) + abs(y):
            return True
    return False