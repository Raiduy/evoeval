
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
    if len(dict) == 0:
        return False
    keys = list(dict.keys())
    first_key = keys[0]
    is_lower = first_key.islower()
    is_upper = first_key.isupper()
    for key in keys[1:]:
        if is_lower and (not key.islower()) or (is_upper and (not key.isupper())):
            return False
    return True