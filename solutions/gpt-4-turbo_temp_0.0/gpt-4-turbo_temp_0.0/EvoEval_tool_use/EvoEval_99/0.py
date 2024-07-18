def checkAlpha(s):
    """Helper Function 1
    This function takes a string s as input and return a string containing only letters by eliminating all the non-alphabetical characters.

    Examples:
        checkAlpha("hello1") => "hello"
        checkAlpha("123") => ""
        checkAlpha("wo3rld.") => "world"
    """
    result = ""
    for char in s:
        if char.isalpha():
            result += char
    return result

def checkLower(s):
    """Helper Function 2
    This function takes a string s as input and returns a string containing only lowercase letters by eliminating all the uppercase letters.

    Examples:
        checkAlpha("Hello") => "ello"
        checkAlpha("WORLD") => ""
        checkAlpha("WorLd") => "ord"
    """
    result = ""
    for char in s:
        if char.islower():
            result += char
    return result
def lowerAlphaDigitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the ASCII codes of the lowercase alphabetical characters only.

    Examples:
        lowerAlphaDigitSum("aBcD") => 196
        lowerAlphaDigitSum("abc123") => 294
        lowerAlphaDigitSum("HELLO") => 0
        lowerAlphaDigitSum("hello$%^&") => 532
        lowerAlphaDigitSum("w3or5ld.") => 552
    """
    result = 0
    for char in s:
        if char.islower():
            result += ord(char)
    return result