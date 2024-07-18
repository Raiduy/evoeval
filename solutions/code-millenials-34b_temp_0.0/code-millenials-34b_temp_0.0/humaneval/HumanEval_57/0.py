

def monotonic(l: list):
    if len(l) < 2:
        return True

    increasing = None
    for i in range(len(l) - 1):
        diff = l[i + 1] - l[i]
        if diff == 0:
            continue
        if increasing is None:
            increasing = diff > 0
        else:
            if (diff > 0) != increasing:
                return False
    return True
