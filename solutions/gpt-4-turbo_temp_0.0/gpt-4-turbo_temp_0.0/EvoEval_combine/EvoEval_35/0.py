def check_dict_happiness(dict):
    if not dict:
        return False
    all_lower = all((key.islower() for key in dict.keys()))
    all_upper = all((key.isupper() for key in dict.keys()))
    if not (all_lower or all_upper):
        return False

    def is_happy_string(s):
        if len(s) < 3:
            return False
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
                return False
        return True
    for key in dict.keys():
        if not isinstance(key, str) or not is_happy_string(key):
            return False
    return True