
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    # Calculate the cube root of the absolute value of a
    cube_root = abs(a) ** (1/3)
    
    # Round the cube root to the nearest integer
    rounded_cube_root = round(cube_root)
    
    # Check if the cube of the rounded cube root equals the absolute value of a
    if rounded_cube_root ** 3 == abs(a):
        return True
    else:
        return False
