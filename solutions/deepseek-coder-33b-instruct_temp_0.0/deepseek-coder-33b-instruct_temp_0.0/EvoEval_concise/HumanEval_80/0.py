
def is_happy(s):
    """
    Determine if the string 's' is 'happy'. A 'happy' string has a length of at least 3 and all 3 consecutive letters are unique. 
    Example: 
    is_happy('a') => False
    is_happy('aa') => False
    is_happy('abcd') => True
    is_happy('aabb') => False
    is_happy('adb') => True
    is_happy('xyy') => False
    """
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) != 3:
            return False
    return True