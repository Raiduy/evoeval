
def closest_integer(value):
    num = float(value)
    if num >= 0:
        if num - int(num) < 0.5:
            return int(num)
        else:
            return int(num) + 1
    elif int(num) - num < 0.5:
        return int(num)
    else:
        return int(num) - 1