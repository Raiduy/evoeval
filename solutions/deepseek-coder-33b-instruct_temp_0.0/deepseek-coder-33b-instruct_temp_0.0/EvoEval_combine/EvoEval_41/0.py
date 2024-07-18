
def shifted_upper_count(s, shift):
    """
    Given a string s and an integer shift, perform a circular shift on the ASCII values of the characters in string 
    by the shift value. Return the count of uppercase vowels in even indices after the shift.

    If shift > length of string, reverse the string before counting.

    For example:
    shifted_upper_count('aBCdEf', 1) returns 0
    shifted_upper_count('abcdefg', 2) returns 0
    shifted_upper_count('dBBE', 3) returns 1
    """
    vowels = 'AEIOU'
    if shift > len(s):
        s = s[::-1]
    else:
        s = s[-shift:] + s[:-shift]
    return sum((1 for (i, c) in enumerate(s) if i % 2 == 0 and c in vowels))