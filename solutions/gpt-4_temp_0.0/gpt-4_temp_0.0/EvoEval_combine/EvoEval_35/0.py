def check_dict_happiness(dict):
    """
    Given a dictionary, where all keys are strings, return True if the following conditions are met:
    1. All keys are either all lower case or all upper case.
    2. Each key is a happy string. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    The function should return False if the given dictionary is empty or if any of the conditions are not met.
    Examples:
    check_dict_happiness({"abc":"apple", "def":"banana"}) should return True.
    check_dict_happiness({"abc":"apple", "ABD":"banana"}) should return False.
    check_dict_happiness({"aab":"apple", "abc":"banana"}) should return False.
    check_dict_happiness({"aab":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_happiness({"ABC":"John", "DEF":"36", "GHI":"Houston"}) should return True.
    check_dict_happiness({"STATE":"NC", "ZIP":"12345" }) should return False.
    """
    if not dict:
        return False
    is_lower = dict.keys()[0].islower()
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if is_lower and key.isupper() or (not is_lower and key.islower()):
            return False
        if len(key) < 3:
            return False
        for i in range(len(key) - 2):
            if key[i] == key[i + 1] or key[i] == key[i + 2] or key[i + 1] == key[i + 2]:
                return False
    return True