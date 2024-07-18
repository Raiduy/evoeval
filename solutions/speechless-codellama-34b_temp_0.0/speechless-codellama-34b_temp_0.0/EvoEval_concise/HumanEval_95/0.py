
def check_dict_case(dictionary):
    if not dictionary:
        return True
    else:
        for key in dictionary.keys():
            if not isinstance(key, str):
                return False
            elif key.islower() or key.isupper():
                continue
            else:
                return False
        return True