
def check_dict_case(dict):
    if not dict:
        return False
    all_lower = all_upper = True
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if not key.islower():
            all_lower = False
        if not key.isupper():
            all_upper = False
    return all_lower or all_upper