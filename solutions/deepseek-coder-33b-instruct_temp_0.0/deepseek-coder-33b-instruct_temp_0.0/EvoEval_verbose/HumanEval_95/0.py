
def check_dict_case(dict):
    """
    Given a dictionary as an input, this function will examine the keys of the dictionary and return a boolean value
    based on certain conditions. 

    Firstly, the function will check if the dictionary is empty. If it is, the function will immediately return False.
    This is because an empty dictionary does not meet the requirements of having all keys in either lower or upper case.

    Then, the function will inspect each key of the dictionary. If all keys are strings that are either entirely in lower 
    case or entirely in upper case, the function will return True. This indicates that the dictionary meets the condition of
    having all keys in a single, consistent case.

    Otherwise, if the keys mix lower and upper case characters, or if non-string keys are found, the function will return 
    False. This indicates that the dictionary does not meet the requirement of keys being in a uniform case.

    For example:

    An input of check_dict_case({"a":"apple", "b":"banana"}) should return True. As all dictionary keys are in lower case. 

    An input of check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False. As dictionary keys here are
    not uniformly in lower or upper case.

    An input of check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False. As one of the dictionary keys 
    is a non-string, which doesn't meet the requirement of all keys being in either lower or upper case strings.

    An input of check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False. As all dictionary keys 
    are not in lower case, nor are they all in upper case.

    An input of check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True. As all dictionary keys here are in upper 
    case.
    """
    if not dict:
        return False
    is_lower = all((key.islower() for key in dict.keys() if isinstance(key, str)))
    is_upper = all((key.isupper() for key in dict.keys() if isinstance(key, str)))
    return is_lower or is_upper