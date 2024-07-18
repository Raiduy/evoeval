
def right_angle_triangle(a, b, c):
    """
    This function takes in three numeric values representing the lengths of the 
    three sides of a potential triangle. It returns a boolean value indicating 
    whether these three sides could compose a right-angled triangle.

    A right-angled triangle, or right triangle, is a type of triangle where one 
    of its angles measures exactly 90 degrees. The relationship between the lengths 
    of the sides of a right triangle is defined by the Pythagorean theorem: the square 
    of the length of the hypotenuse (the side opposite the right angle) is equal to 
    the sum of the squares of the lengths of the other two sides. This function uses 
    this theorem to determine if the three given sides can form a right triangle.

    Parameters:
    a (numeric): The length of the first side of the potential triangle.
    b (numeric): The length of the second side of the potential triangle.
    c (numeric): The length of the third side of the potential triangle.

    Returns:
    boolean: True if the three sides can form a right triangle, False otherwise.

    Examples:
    right_angle_triangle(3, 4, 5) == True
    In this case, 3*3 + 4*4 = 5*5, so the sides form a right triangle.

    right_angle_triangle(1, 2, 3) == False
    In this case, 1*1 + 2*2 != 3*3, so the sides do not form a right triangle.
    """
    sides = sorted([a, b, c])
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2