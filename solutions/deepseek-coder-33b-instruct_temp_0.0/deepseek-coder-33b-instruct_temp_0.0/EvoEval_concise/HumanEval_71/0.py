
def triangle_area(a, b, c):
    """
    Returns area of a triangle (rounded to 2 decimals) given the lengths of its 
    three sides, if they form a valid triangle. If not, returns -1. A valid triangle 
    is one where the sum of any two sides is greater than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """
    if a + b > c and a + c > b and (b + c > a):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1