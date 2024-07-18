
def closest_integer(value):
    value = float(value)
    if value >= 0:
        return int(value)
    else:
        return int(value) if value == int(value) else int(value) - 1