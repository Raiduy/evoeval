
def digitSum(s):
    """
    Given a string 's', the function returns the sum of the ASCII values of the uppercase characters in 's'.
    
    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum((ord(c) for c in s if c.isupper()))