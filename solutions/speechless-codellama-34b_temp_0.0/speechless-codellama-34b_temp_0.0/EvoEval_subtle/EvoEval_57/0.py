

def monotonic(l: list):
    if not l:
        return False
    elif len(l) == 1:
        return True
    else:
        diff = l[1] - l[0]
        for i in range(2, len(l)):
            if (l[i] - l[i - 1]) * diff < 0:
                return False
        return True