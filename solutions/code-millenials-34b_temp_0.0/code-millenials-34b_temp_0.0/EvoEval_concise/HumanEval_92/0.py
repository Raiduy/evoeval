
def any_int(x, y, z):
    if all((isinstance(i, int) for i in [x, y, z])):
        return any([x + y == z, x + z == y, y + z == x])
    else:
        return False