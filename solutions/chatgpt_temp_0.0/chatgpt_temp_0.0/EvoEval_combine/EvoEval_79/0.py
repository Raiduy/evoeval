
def happy_case_string(s):
    if len(s) < 3:
        return s[::-1]
    happy = True
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            happy = False
            break
    if not happy or not any((c.isalpha() for c in s)):
        return s[::-1]
    result = ''
    for c in s:
        if c.isalpha():
            if c.islower():
                result += c.upper()
            else:
                result += c.lower()
        else:
            result += c
    return result[::-1]