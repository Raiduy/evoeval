def iscube(a, b):
    if a < 0 or b < 0:
        return False
    a_cube = round(a ** (1 / 3))
    if a != a_cube ** 3:
        return False
    b_square = round(b ** 0.5)
    if b != b_square ** 2:
        return False
    if (a + b) % 2 != 0:
        return False
    return True