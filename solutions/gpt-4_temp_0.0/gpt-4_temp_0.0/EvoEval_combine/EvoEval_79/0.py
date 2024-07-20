
def happy_case_string(s):

    def is_happy(s):
        if len(s) < 3:
            return False
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
                return False
        return True
    if is_happy(s):
        return ''.join([c.upper() if c.islower() else c.lower() for c in s])
    else:
        return s[::-1]