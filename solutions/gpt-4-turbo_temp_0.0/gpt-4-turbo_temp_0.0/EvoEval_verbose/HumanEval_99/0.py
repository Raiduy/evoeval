
def closest_integer(value):
    num = float(value)
    fractional_part = abs(num) - abs(int(num))
    if fractional_part == 0.5:
        if num > 0:
            return int(num) + 1
        else:
            return int(num) - 1
    else:
        return round(num)