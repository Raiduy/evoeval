
def median(l: list):
    if not l:
        return 0
    l.sort()
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]