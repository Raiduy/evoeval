
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
    # Taking the cube root of a. For negative numbers, consider the absolute value for cube root calculation
    # and then multiply by -1 to maintain the sign.
    cube_root = abs(a) ** (1/3)
    
    # Check if the cube root, when rounded to the nearest integer, cubed, is equal to the original number.
    # This accounts for floating point arithmetic issues.
    if round(cube_root) ** 3 == abs(a):
        return True
    else:
        return False
