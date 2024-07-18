
def check_dict_case(dict):
    """
    Returns True if all keys in the input dictionary are either all lower case or all upper case strings. 
    If the dictionary is empty or if the keys are a mix of upper and lower case strings, the function returns False.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) returns True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) returns False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) returns False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) returns False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) returns True.
    """
    if not dict:
        return False
    all_lower = all_upper = None
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if all_lower is None and all_upper is None:
            all_lower = key.islower()
            all_upper = key.isupper()
        else:
            if all_lower and (not key.islower()):
                return False
            if all_upper and (not key.isupper()):
                return False
    return True