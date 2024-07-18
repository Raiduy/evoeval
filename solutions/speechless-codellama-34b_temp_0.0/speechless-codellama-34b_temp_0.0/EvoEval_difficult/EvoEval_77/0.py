def iscube(a, b):
    if a < 0 or b < 0:
        return False
    a_cube_root = round(a ** (1 / 3))
    b_square_root = round(b ** 0.5)
    return a == a_cube_root ** 3 and b == b_square_root ** 2 and ((a + b) % 2 == 0)