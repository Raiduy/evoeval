
def iscube(a):
    if a < 0:
        return False
    else:
        return round(a ** (1.0 / 3)) ** 3 == a