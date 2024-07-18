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
            if len(set(key[i:i + 3])) != 3:
                return False
    return True