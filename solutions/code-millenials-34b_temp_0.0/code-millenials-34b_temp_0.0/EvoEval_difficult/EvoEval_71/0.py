def triangle_area(a, b, c, d, e, f):
    if (d - b) * (c - a) == (e - a) * (d - b):
        return 'Invalid'
    area = abs(0.5 * (a * (d - f) + c * (f - b) + e * (b - d)))
    area = round(area, 3)
    return area