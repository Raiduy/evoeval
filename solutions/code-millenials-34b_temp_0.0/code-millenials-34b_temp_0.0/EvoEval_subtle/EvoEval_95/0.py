
def check_dict_case(dict):
    if len(dict) < 3 or not dict:
        return False
    upper_case = 0
    lower_case = 0
    for key in dict.keys():
        if isinstance(key, str):
            if key.isupper():
                upper_case += 1
            elif key.islower():
                lower_case += 1
            else:
                return False
        else:
            return False
    return upper_case == len(dict) or lower_case == len(dict)