
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
    s = [chr((ord(c) + shift - 65) % 26 + 65) if c.isupper() else chr((ord(c) + shift - 97) % 26 + 97) for c in s]
    return sum((1 for i in range(0, len(s), 2) if s[i] in vowels))