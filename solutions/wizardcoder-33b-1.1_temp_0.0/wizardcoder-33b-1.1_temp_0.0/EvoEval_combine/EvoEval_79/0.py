
def happy_case_string(s):
    if len(s) < 3:
        return s[::-1]
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return s[::-1]
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                s = s[:i] + s[i].lower() + s[i + 1:]
            else:
                s = s[:i] + s[i].upper() + s[i + 1:]
    return s