
def solve(s):
    has_alpha = any((c.isalpha() for c in s))
    if has_alpha:
        return ''.join((c.upper() if c.islower() else c.lower() for c in s))
    else:
        return s[::-1]