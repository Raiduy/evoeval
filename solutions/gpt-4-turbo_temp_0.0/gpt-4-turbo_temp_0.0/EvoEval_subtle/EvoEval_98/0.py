
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in odd indices.
    
    For example:
    count_upper('aBCdEf') returns 0
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 1
    """
    vowels = 'AEIOU'
    count = 0
    for i in range(1, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count