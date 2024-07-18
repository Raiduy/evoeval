
def solve(s):
    has_letter = any((c.isalpha() for c in s))
    if has_letter:
        return ''.join((c.upper() if c.islower() else c.lower() if c.isupper() else c for c in s))
    else:
        return s[::-1]