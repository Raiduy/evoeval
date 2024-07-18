
def happy_case_string(s):
    if len(s) < 3:
        return s[::-1]
    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) != 3:
            return s[::-1]
    return ''.join([c.upper() if c.islower() else c.lower() if c.isupper() else c for c in s])