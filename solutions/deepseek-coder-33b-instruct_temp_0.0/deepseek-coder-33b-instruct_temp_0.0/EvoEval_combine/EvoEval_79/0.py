
def happy_case_string(s):
    if len(s) < 3:
        return s[::-1]
    for i in range(len(s) - 2):
        if s[i].lower() == s[i + 1].lower() or s[i].lower() == s[i + 2].lower() or s[i + 1].lower() == s[i + 2].lower():
            return s[::-1]
    result = ''
    for char in s:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result