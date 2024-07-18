
def count_upper(s):
    """
    Returns the count of uppercase vowels at even indices in string s.
    
    Example:
    count_upper('aBCdEf') -> 1
    count_upper('abcdefg') -> 0
    count_upper('dBBE') -> 0
    """
    upper_vowels = 'AEIOU'
    return sum((1 for i in range(len(s)) if i % 2 == 0 and s[i] in upper_vowels))