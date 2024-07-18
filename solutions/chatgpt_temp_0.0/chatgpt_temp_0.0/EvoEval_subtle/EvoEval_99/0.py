
def closest_integer(value):
    value = float(value)
    floor = int(value)
    ceiling = floor + 1
    distance_floor = abs(value - floor)
    distance_ceiling = abs(value - ceiling)
    if distance_floor == distance_ceiling:
        return floor if value >= 0 else ceiling
    return floor if distance_floor < distance_ceiling else ceiling