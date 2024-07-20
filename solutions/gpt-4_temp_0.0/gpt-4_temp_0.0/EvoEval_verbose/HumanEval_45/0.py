

def triangle_area(a, h):
    """
    Calculates and returns the area of a triangle based on the length of one side and the height from that side to the opposite vertex.

    This function takes two parameters: the length of a side (a) and the height (h). The length of a side and the height must be non-negative numbers. If other types of inputs are given, the function may behave unpredictably.

    The area of the triangle is calculated with the formula '0.5 * a * h'. This formula is derived from the geometric characteristics of the triangle.

    Args:
    a (float): The length of a side of the triangle. Must be a non-negative number.
    h (float): The height from one side to the opposite vertex. Must be a non-negative number.

    Returns:
    float: The area of the triangle. Returns a floating point number that represents the calculated area.

    Example:
    >>> triangle_area(5, 3)
    7.5

    The example demonstrates that if the length of a side of the triangle is 5 and the height from that side to the opposite vertex is 3, the function returns the area of the triangle, which is 7.5.
    """
    return 0.5 * a * h