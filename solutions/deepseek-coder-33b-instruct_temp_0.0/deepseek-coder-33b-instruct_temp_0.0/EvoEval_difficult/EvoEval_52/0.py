def below_above_threshold(l: list, t1: int, t2: int, s: str):
    if s == 'below':
        for i in range(len(l)):
            if l[i] >= t1:
                return i
        return True
    elif s == 'above':
        for i in range(len(l)):
            if l[i] <= t2:
                return i
        return True
    else:
        return -1