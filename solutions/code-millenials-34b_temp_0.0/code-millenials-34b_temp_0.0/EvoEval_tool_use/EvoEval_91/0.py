def parse_string(s):
    '''
    This helper function takes a string and removes all non-alphabet characters.
    
    Args:
    s: A string
    
    Returns:
    A string having only alphabet characters.
    
    Example:
    
    parse_string("Hello, World!") ➞ "HelloWorld"
    parse_string("Pyth0n Pr0gramm!ng") ➞ "PythonProgramming"
    '''
    return ''.join(c for c in s if c.isalpha())
def rearrange_string(s1, s2):
    s1 = parse_string(s1)
    s2 = parse_string(s2)
    ascii_sum_s1 = sum((ord(c) for c in s1))
    ascii_sum_s2 = sum((ord(c) for c in s2))
    if ascii_sum_s1 <= ascii_sum_s2:
        return ''.join(sorted(s1 + s2))
    else:
        return ''.join(sorted(s1 + s2, reverse=True))