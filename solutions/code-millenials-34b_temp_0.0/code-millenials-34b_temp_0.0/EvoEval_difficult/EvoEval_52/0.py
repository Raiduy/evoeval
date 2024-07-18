def below_above_threshold(l: list, t1: int, t2: int, s: str):
    if s == 'below':
        for (i, num) in enumerate(l):
            if num >= t1:
                return i
        return True
    elif s == 'above':
        for (i, num) in enumerate(l):
            if num <= t2:
                return i
        return True
    else:
        return -1