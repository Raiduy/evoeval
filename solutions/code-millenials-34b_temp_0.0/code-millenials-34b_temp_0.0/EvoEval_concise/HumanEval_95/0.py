
def check_dict_case(dict):
    if not dict:
        return True
    all_upper = all((k.isupper() for k in dict.keys()))
    all_lower = all((k.islower() for k in dict.keys()))
    return all_upper or all_lower