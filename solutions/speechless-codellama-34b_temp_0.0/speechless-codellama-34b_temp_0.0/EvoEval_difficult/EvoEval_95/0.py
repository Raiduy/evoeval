def check_dict_case_content(dictionary):
    if not dictionary:
        return False
    key_length = len(next(iter(dictionary.keys())))
    for (key, value) in dictionary.items():
        if not isinstance(key, str) or not isinstance(value, str):
            return False
        if len(key) != key_length:
            return False
        if key.islower() and value.istitle():
            continue
        if key.isupper() and value.istitle():
            continue
        return False
    return True