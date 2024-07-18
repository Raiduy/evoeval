
def count_upper(s):
    """
    The function count_upper(s) takes a single argument, s which is a string.

    The purpose of this function is to determine and return the number of uppercase vowels that are present at even indices 
    in the input string s.

    The function iterates over all even indices of the input string and checks if the character at those positions is an 
    uppercase vowel (A, E, I, O, U). It maintains a count of such characters and finally returns this count.

    The function does not modify the input string and only performs read operations on it. The input string can include any 
    printable ASCII character. The input string is zero-indexed, meaning the first character of the string is considered to be 
    at index 0, the second character at index 1, and so on. As per this function's requirements, any uppercase vowel at index 0, 
    2, 4, and so forth is considered.

    For instance:
    If the input string s is 'aBCdEf', the function count_upper('aBCdEf') returns 1, because 'E' is an uppercase vowel and is 
    present at an even index
    If the input string s is 'abcdefg', the function count_upper('abcdefg') returns 0, because there are no uppercase vowels at even indices.
    If the input string s is 'dBBE', the function count_upper('dBBE') returns 0, because despite having uppercase vowels, none of 
    them are located at even indices.
    """
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU':
            count += 1
    return count