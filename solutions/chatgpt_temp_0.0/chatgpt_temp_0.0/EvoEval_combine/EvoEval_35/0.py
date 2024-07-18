def check_dict_happiness(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    first_key = keys[0]
    is_lower = first_key.islower()
    is_upper = first_key.isupper()
    if not all((key.islower() == is_lower or key.isupper() == is_upper for key in keys)):
        return False

    def is_happy_string(s):
        if len(s) < 3:
            return False
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
                return False
        return True
    return all((is_happy_string(key) for key in keys))