
def triangle_area(a, b, c):
    """
    This function calculates and returns the area of a triangle, given the lengths of the three sides (a, b, c). 
    The parameters a, b, c represent the lengths of the sides of a triangle, and they should be supplied as numerical 
    values (either integers or floating point numbers). 

    The function uses Heron's formula to compute the area. However, before the calculation, the function 
    checks if the given side lengths form a valid triangle. Validity of a triangle is determined by the triangle 
    inequality theorem which states that the sum of the lengths of any two sides of a triangle must be greater than the 
    length of the third side. If the side lengths do not form a valid triangle, the function returns -1.

    The computed area of the triangle is then returned, rounded to 2 decimal places.

    Example:
    If the function is called with the arguments (3, 4, 5), it should return 6.00. This is because 3, 4, 5 are the side 
    lengths of a right triangle, and the area of this triangle is 6 square units. So, the output of triangle_area(3, 4, 5) 
    should be 6.00.

    If the function is called with the arguments (1, 2, 10), it should return -1. This is because 1, 2, 10 do not form a 
    valid triangle according to the triangle inequality theorem (since 1 + 2 is not greater than 10). So, the output of 
    triangle_area(1, 2, 10) should be -1.
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return round(area, 2)