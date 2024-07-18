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
    s1 = ''.join((c for c in s1 if c.isalpha()))
    s2 = ''.join((c for c in s2 if c.isalpha()))
    sum1 = sum((ord(c) for c in s1))
    sum2 = sum((ord(c) for c in s2))
    result = s1 + s2
    if sum1 <= sum2:
        result = ''.join(sorted(result))
    else:
        result = ''.join(sorted(result, reverse=True))
    return result