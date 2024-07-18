
def solve_and_count(s):
    has_letters = any((c.isalpha() for c in s))
    if not has_letters:
        return (s[::-1], 0)
    result = ''
    for c in s:
        if c.isalpha():
            result += c.lower() if c.isupper() else c.upper()
        else:
            result += c
    count = sum((1 for i in range(0, len(result), 2) if result[i] in 'AEIOU'))
    return (result, count)