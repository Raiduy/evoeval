

def monotonic(l: list):
    if len(l) == 0:
        return False
    if len(l) == 1:
        return True
    if l[0] <= l[1]:
        for i in range(2, len(l)):
            if l[i - 1] > l[i]:
                return False
        return True
    else:
        for i in range(2, len(l)):
            if l[i - 1] < l[i]:
                return False
        return True