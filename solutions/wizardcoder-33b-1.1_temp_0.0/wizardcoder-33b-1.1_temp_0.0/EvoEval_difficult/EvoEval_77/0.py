def iscube(a, b):
    if a < 0 or b < 0:
        return False
    else:
        a_cube_root = round(a ** (1.0 / 3))
        b_square_root = round(b ** 0.5)
        if a_cube_root ** 3 == a and b_square_root ** 2 == b and ((a + b) % 2 == 0):
            return True
        else:
            return False