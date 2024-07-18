def check_dict_happiness(dict):
    if not dict:
        return False
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if not key.islower() and (not key.isupper()):
            return False
        if len(key) < 3:
            return False
        for i in range(len(key) - 2):
            if key[i] == key[i + 1] or key[i] == key[i + 2] or key[i + 1] == key[i + 2]:
                return False
    return True