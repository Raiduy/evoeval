
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty or the number of keys is less than 3.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return False because it has less than 3 keys.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345", "CITY": "New York" }) should return True.
    """
    if not dict or len(dict) < 3:
        return False
    all_lower = all_upper = True
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if not key.islower():
            all_lower = False
        if not key.isupper():
            all_upper = False
    return all_lower or all_upper