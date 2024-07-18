
def any_int(x, y, z):
    if all((isinstance(i, int) for i in [x, y, z])):
        if x == abs(y) + abs(z) or y == abs(x) + abs(z) or z == abs(x) + abs(y):
            return True
    return False