
def happy_case_string(s):

    def is_happy(s):
        if len(s) < 3:
            return False
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
                return False
        return True

    def reverse_case(s):
        return ''.join([c.upper() if c.islower() else c.lower() for c in s])

    def contains_letter(s):
        return any((c.isalpha() for c in s))
    if is_happy(s) and contains_letter(s):
        return reverse_case(s)
    else:
        return s[::-1]