
def iscube(a):
    cube_root = round(a ** (1.0 / 3))
    return cube_root ** 3 == abs(a)