
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
        return s.swapcase()
    else:
        return s[::-1]