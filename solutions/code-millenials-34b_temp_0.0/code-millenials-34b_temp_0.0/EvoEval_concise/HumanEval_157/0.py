
def right_angle_triangle(a, b, c):
    longest = max(a, b, c)
    sum_squares = a ** 2 + b ** 2 + c ** 2 - longest ** 2
    return longest ** 2 == sum_squares