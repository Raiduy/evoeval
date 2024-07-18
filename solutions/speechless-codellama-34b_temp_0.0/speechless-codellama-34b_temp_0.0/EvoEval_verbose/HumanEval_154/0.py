
def cycpattern_check(a, b):
    n = len(b)
    for i in range(n):
        if b in a:
            return True
        b = b[-1] + b[:-1]
    return False