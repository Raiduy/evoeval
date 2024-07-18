
def choose_num(x, y):
    if x > y:
        return -1
    else:
        max_even = y if y % 2 == 0 else y - 1
        return max_even if max_even >= x else -1