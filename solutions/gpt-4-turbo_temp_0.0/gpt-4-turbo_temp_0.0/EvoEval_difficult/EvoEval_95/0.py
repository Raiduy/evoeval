def check_dict_case_content(dict):
    if not dict:
        return False
    key_case = None
    key_length = None
    for (key, value) in dict.items():
        if not isinstance(key, str) or not isinstance(value, str):
            return False
        if key_case is None:
            key_case = key.islower() or key.isupper()
            key_length = len(key)
        elif (key.islower() or key.isupper()) != key_case or len(key) != key_length:
            return False
        if not (value[0].isupper() and value[1:].islower()):
            return False
    return True