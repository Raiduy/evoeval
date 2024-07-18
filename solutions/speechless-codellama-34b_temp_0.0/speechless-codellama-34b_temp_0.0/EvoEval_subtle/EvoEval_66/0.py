
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the lower characters only'
    ASCII codes.
    """
    return sum((ord(c) for c in s if c.islower()))