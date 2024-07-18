def check_dict_case_content(dict):
    if not dict:
        return False
    key_length = len(next(iter(dict.keys())))
    for (key, value) in dict.items():
        if not isinstance(key, str) or not isinstance(value, str):
            return False
        if not (key.islower() or key.isupper()) or len(key) != key_length:
            return False
        if not value.istitle():
            return False
    return True