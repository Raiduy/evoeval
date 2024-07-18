
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in odd indices.
    
    For example:
    count_upper('aBCdEf') returns 0
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 1
    """
    count = 0
    for i in range(len(s)):
        if i % 2 == 1 and s[i] in 'AEIOU':
            count += 1
    return count