def check_dict_happiness(dict):
    if not dict:
        return False
    case = None
    for key in dict:
        if not isinstance(key, str):
            return False
        if case is None:
            case = key.isupper()
        elif key.isupper() != case:
            return False
        if len(key) < 3 or len(set((key[i:i + 3] for i in range(len(key) - 2)))) != len(key) - 2:
            return False
    return True