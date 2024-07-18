
def right_angle_triangle(a, b, c):
    # compute the sides of the triangle
    sides = [a, b, c]
    sides.sort()
    a, b, c = sides

    # compute the squares of the sides
    squares = [x**2 for x in sides]

    # check if the triangle is right-angled
    return squares[0] + squares[1] == squares[2]
