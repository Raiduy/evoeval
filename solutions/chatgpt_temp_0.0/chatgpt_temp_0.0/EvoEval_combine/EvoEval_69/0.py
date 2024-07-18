def sorted_happy_strings(lst):

    def is_happy_string(s):
        if len(s) < 3:
            return False
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
                return False
        return True
    happy_strings = [s for s in lst if is_happy_string(s) and len(s) % 2 == 0]
    return sorted(happy_strings, key=lambda x: (len(x), x))