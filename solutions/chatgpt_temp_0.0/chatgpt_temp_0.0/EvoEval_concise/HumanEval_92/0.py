
def any_int(x, y, z):
    if not all((isinstance(num, int) for num in [x, y, z])):
        return False
    if x == y + z or y == x + z or z == x + y:
        return True
    return False