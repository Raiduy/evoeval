
def iscube(a):
    if a < 0:
        return False
    cube_root = abs(a) ** (1 / 3)
    rounded_root = round(cube_root)
    return rounded_root ** 3 == a