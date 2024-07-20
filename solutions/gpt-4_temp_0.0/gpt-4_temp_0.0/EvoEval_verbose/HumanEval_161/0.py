
def solve(s):
    if any((char.isalpha() for char in s)):
        return ''.join((char.swapcase() for char in s))
    else:
        return s[::-1]