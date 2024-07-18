

def monotonic(l: list):
    if len(l) < 2:
        return False
    else:
        diff = l[1] - l[0]
        for index in range(2, len(l)):
            if (l[index] - l[index - 1]) * diff < 0:
                return False
        return True