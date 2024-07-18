def check_dict_happiness(dict):

    def is_happy_string(s):
        if len(s) < 3:
            return False
        for i in range(len(s) - 2):
            if len(set(s[i:i + 3])) != 3:
                return False
        return True
    if not dict:
        return False
    keys = dict.keys()
    if not all((k.islower() or k.isupper() for k in keys)):
        return False
    if not all((is_happy_string(k) for k in keys)):
        return False
    return True