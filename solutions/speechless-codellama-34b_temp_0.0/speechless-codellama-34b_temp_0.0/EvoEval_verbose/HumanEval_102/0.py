
def choose_num(x, y):
    if x > y:
        return -1
    else:
        for i in range(y, x - 1, -1):
            if i % 2 == 0:
                return i
        return -1