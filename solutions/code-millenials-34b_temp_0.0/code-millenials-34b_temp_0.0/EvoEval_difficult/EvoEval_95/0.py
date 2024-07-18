def check_dict_case_content(d):
    if not d:
        return False
    keys = list(d.keys())
    values = list(d.values())
    if len(keys) != len(values):
        return False
    for (key, value) in d.items():
        if not isinstance(key, str) or not isinstance(value, str):
            return False
        if key != key.lower() and key != key.upper():
            return False
        if value != value.capitalize():
            return False
    return True