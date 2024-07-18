
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
    lower_case = all((isinstance(key, str) and key.islower() for key in dict.keys()))
    upper_case = all((isinstance(key, str) and key.isupper() for key in dict.keys()))
    return lower_case or upper_case