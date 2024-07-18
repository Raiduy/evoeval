def triangle_area(a, b, c, d, e, f):
    if (d - f) * (c - e) == (b - f) * (e - c):
        return 'Invalid'
    else:
        area = abs(0.5 * (a * (d - f) + c * (f - b) + e * (b - d)))
        return round(area, 3)