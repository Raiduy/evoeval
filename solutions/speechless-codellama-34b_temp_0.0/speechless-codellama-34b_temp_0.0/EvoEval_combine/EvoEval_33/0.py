
def roman_happiness(s):
    roman_numerals = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    if len(s) < 3:
        return False
    total = 0
    for i in range(len(s)):
        if i > 0 and s[i] == s[i - 1]:
            return False
        if i > 1 and s[i] == s[i - 2]:
            return False
        total += roman_numerals[s[i]]
        if total > 1000:
            return False
    return total