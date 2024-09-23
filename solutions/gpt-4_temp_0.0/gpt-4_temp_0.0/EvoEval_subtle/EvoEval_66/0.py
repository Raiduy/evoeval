
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the lower characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 195
        digitSum("abcCd") => 394
        digitSum("helloE") => 532
        digitSum("woArBld") => 652
        digitSum("aAaaaXa") => 485
    """
    return sum((ord(c) for c in s if c.islower()))