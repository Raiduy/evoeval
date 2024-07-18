
def right_angle_triangle(a, b, c):
    """
    Determine if the lengths of the three sides of a triangle form a right-angled triangle.
    A triangle has a right angle if the square of the longest side equals the sum of the squares of the other two sides.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    sides = [a, b, c]
    sides.sort()
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2