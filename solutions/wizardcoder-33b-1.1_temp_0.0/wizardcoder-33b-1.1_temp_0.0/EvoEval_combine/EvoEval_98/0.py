
def check_dict_bracketing(dict):
    if not dict:
        return False
    keys_case = None
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if keys_case is None:
            keys_case = key.islower()
        elif keys_case != key.islower():
            return False
    for value in dict.values():
        if not isinstance(value, str):
            return False
        if value.count('(') != value.count(')'):
            return False
    return True