def any_int_complex(x, y, z):
    if not (isinstance(x, int) or str(x).isdigit()):
        return 'Invalid Input'
    if not (isinstance(y, int) or str(y).isdigit()):
        return 'Invalid Input'
    if not (isinstance(z, int) or str(z).isdigit()):
        return 'Invalid Input'
    x = int(x)
    y = int(y)
    z = int(z)
    if x == y + z or y == x + z or z == x + y:
        return True
    else:
        return False