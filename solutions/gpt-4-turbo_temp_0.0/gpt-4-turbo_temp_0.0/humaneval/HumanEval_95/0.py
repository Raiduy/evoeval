
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    # Check if the dictionary is empty
    if not dict:
        return False
    
    # Initialize variables to track the case of keys
    all_lower = all_upper = True
    
    for key in dict.keys():
        # Check if the key is a string, if not return False
        if not isinstance(key, str):
            return False
        
        # Check the case of the key
        if key.islower():
            all_upper = False
        elif key.isupper():
            all_lower = False
        else:
            # If the key is neither all lower nor all upper case, return False
            return False
        
        # If both flags are False, it means we have a mix of upper and lower case keys
        if not all_lower and not all_upper:
            return False
    
    return True
