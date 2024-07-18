
def solve(s):
    if any((char.isalpha() for char in s)):
        return ''.join((c.upper() if c.islower() else c.lower() for c in s))
    else:
        return s[::-1]