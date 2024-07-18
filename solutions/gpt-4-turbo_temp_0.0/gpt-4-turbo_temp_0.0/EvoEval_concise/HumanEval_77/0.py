
def iscube(a):
    """
    Determines if an integer is a perfect cube.
    
    Accepts an integer and returns True if it's a perfect cube, else False.
    Input will always be valid.
    
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    """
    cube_root = abs(a) ** (1 / 3)
    return round(cube_root) ** 3 == abs(a) and (a >= 0 or round(cube_root) ** 3 == -a)