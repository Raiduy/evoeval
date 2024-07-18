
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only'
    ASCII codes.
    """
    sum = 0
    for char in s:
        if char.isupper():
            sum += ord(char)
    return sum
