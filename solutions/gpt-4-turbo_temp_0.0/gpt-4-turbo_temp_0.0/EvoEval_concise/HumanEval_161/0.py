
def solve(s):
    """
    Given a string 's', if 's' contains alphabetic characters, flip their case. If 's' contains no alphabetic characters, reverse 's'. 
    Return the modified string.
    Examples:
    solve("1234") -> "4321"
    solve("ab") -> "AB"
    solve("#a@C") -> "#A@c"
    """
    if any((c.isalpha() for c in s)):
        return ''.join((c.lower() if c.isupper() else c.upper() for c in s))
    else:
        return s[::-1]