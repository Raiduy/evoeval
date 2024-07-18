
def check_dict_bracketing(dict):
    if not dict:
        return False
    lower_case = all((key.islower() for key in dict.keys()))
    upper_case = all((key.isupper() for key in dict.keys()))
    if not (lower_case or upper_case):
        return False
    for value in dict.values():
        if not all((c in '()' for c in value)):
            return False
        if value.count('(') != value.count(')'):
            return False
    return True