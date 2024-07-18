
def check_dict_bracketing(dict):
    if not dict:
        return False
    if not all((k.islower() for k in dict.keys())) and (not all((k.isupper() for k in dict.keys()))):
        return False
    for v in dict.values():
        if not all((c in '()' for c in v)):
            return False
        if v.count('(') != v.count(')'):
            return False
    return True