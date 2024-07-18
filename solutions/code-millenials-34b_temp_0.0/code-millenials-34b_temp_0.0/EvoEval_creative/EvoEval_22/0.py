def galactic_travel(t, v):
    light_year = 9.461 * 10 ** 12
    distance = t * v
    distance_ly = distance / light_year
    return round(distance_ly, 15)