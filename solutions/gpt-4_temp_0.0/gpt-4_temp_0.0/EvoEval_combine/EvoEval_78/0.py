
def solve_and_count(s):
    if not any((c.isalpha() for c in s)):
        return (s[::-1], 0)
    else:
        s = s.swapcase()
        vowels = 'AEIOU'
        count = sum((1 for i in range(0, len(s), 2) if s[i] in vowels))
        return (s, count)