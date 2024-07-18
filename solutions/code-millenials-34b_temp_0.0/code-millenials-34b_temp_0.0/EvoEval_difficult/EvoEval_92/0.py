def any_int_complex(x, y, z):
    try:
        x = int(x)
        y = int(y)
        z = int(z)
    except ValueError:
        return 'Invalid Input'
    if x + y == z or x + z == y or y + z == x:
        return True
    else:
        return False