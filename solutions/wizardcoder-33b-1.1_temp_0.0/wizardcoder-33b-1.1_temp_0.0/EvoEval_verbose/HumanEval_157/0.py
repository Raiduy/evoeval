
def right_angle_triangle(a, b, c):
    (a, b, c) = sorted([a, b, c], reverse=True)
    return a ** 2 == b ** 2 + c ** 2