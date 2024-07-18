def triangle_area(vertices):
    side1 = ((vertices[0][0] - vertices[1][0]) ** 2 + (vertices[0][1] - vertices[1][1]) ** 2) ** 0.5
    side2 = ((vertices[0][0] - vertices[2][0]) ** 2 + (vertices[0][1] - vertices[2][1]) ** 2) ** 0.5
    side3 = ((vertices[1][0] - vertices[2][0]) ** 2 + (vertices[1][1] - vertices[2][1]) ** 2) ** 0.5
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return 'Not a triangle'
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return area