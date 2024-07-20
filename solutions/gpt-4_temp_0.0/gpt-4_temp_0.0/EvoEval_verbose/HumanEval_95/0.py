
def check_dict_case(dict):
    """
    Given a dictionary as an input, this function will examine the keys of the dictionary and return a boolean value
    based on certain conditions. 
    """
    if not dict:
        return False
    first_key_case = None
    for key in dict:
        if not isinstance(key, str):
            return False
        if first_key_case is None:
            if key.islower():
                first_key_case = 'lower'
            elif key.isupper():
                first_key_case = 'upper'
            else:
                return False
        elif first_key_case == 'lower' and (not key.islower()):
            return False
        elif first_key_case == 'upper' and (not key.isupper()):
            return False
    return True