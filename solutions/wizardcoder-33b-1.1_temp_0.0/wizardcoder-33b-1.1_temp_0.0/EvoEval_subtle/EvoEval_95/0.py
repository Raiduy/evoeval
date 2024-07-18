
def check_dict_case(dict):
    if len(dict) < 3:
        return False
    case = None
    for key in dict:
        if not isinstance(key, str):
            return False
        if case is None:
            case = key.islower()
        elif key.islower() and (not case) or (not key.islower() and case):
            return False
    return True