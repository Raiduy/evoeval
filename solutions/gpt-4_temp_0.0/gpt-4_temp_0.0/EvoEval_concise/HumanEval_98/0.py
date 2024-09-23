
def count_upper(s):
    """
    Returns the count of uppercase vowels at even indices in string s.
    
    Example:
    count_upper('aBCdEf') -> 1
    count_upper('abcdefg') -> 0
    count_upper('dBBE') -> 0
    """
    count = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in range(0, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count