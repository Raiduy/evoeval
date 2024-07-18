
def check_dict_case(dictionary):
    if not dictionary:
        return False
    for key in dictionary:
        if not isinstance(key, str):
            return False
        if not key.islower() and (not key.isupper()):
            return False
    return True