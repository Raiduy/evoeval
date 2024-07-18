def triangle_area(a, b, c, d, e, f):
    if (d - b) * (c - a) == (f - b) * (e - a):
        return 'Invalid'
    else:
        area = 0.5 * abs(a * (d - f) + c * (f - b) + e * (b - d))
        return round(area, 3)