def iscube(a, b):
    if a < 0 or b < 0:
        return False
    else:
        import math
        a_cube_check = round(a ** (1.0 / 3)) ** 3 == a
        b_square_check = math.sqrt(b).is_integer()
        sum_even_check = (a + b) % 2 == 0
        return a_cube_check and b_square_check and sum_even_check