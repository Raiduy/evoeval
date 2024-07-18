def iscube(a, b):
    if a < 0 or b < 0:
        return False
    if a ** (1 / 3) % 1 != 0 or b ** (1 / 2) % 1 != 0:
        return False
    if (a + b) % 2 != 0:
        return False
    return True