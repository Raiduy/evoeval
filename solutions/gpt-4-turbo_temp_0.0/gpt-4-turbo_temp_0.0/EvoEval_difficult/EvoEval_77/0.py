def iscube(a, b):
    if a < 0 or b < 0:
        return False
    a_cube_root = round(a ** (1 / 3))
    is_a_cube = a_cube_root ** 3 == a
    b_square_root = round(b ** 0.5)
    is_b_square = b_square_root ** 2 == b
    is_sum_even = (a + b) % 2 == 0
    return is_a_cube and is_b_square and is_sum_even