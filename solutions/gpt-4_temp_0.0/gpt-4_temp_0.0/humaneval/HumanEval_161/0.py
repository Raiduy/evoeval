
def solve(s):
    if not any(char.isalpha() for char in s):
        return s[::-1]
    else:
        return ''.join(char.lower() if char.isupper() else char.upper() for char in s)
