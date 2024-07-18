
def happy_case_string(s):
    if len(s) < 3:
        return s[::-1]
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
            return s[::-1]
    new_s = ''
    for c in s:
        if c.isalpha():
            new_s += c.lower() if c.isupper() else c.upper()
        else:
            new_s += c
    return new_s