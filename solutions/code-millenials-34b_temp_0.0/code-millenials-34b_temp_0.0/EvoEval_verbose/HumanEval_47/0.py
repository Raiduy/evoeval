

def median(l: list):
    n = len(l)
    s = sorted(l)
    return (s[n // 2] + s[-(n + 1) // 2]) / 2