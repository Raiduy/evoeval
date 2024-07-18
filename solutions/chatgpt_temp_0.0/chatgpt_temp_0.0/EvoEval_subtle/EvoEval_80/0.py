
def is_happy(s):
    if len(s) < 4:
        return False
    for i in range(len(s) - 3):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i] == s[i + 3] or (s[i + 1] == s[i + 2]) or (s[i + 1] == s[i + 3]) or (s[i + 2] == s[i + 3]):
            return False
    return True