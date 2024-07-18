
def check_dict_case(dict):
    if not dict:
        return False
    is_lower = all((key.islower() for key in dict.keys() if isinstance(key, str)))
    is_upper = all((key.isupper() for key in dict.keys() if isinstance(key, str)))
    return is_lower or is_upper