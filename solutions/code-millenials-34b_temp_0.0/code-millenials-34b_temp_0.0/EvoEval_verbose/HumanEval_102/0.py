
def choose_num(x, y):
    if x > y or x < 0 or y < 0:
        return -1
    if x % 2 == 0 and y % 2 == 0:
        return y
    elif y % 2 == 0:
        return y
    else:
        return y - 1