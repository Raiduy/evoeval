def check_dict_case_content(dict):
    if not dict or len(set(map(len, dict.keys()))) != 1:
        return False
    for (key, value) in dict.items():
        if not isinstance(key, str) or not isinstance(value, str):
            return False
        if not (key.islower() or key.isupper()):
            return False
        if not (value[0].isupper() and value[1:].islower()):
            return False
    return True