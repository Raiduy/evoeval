
def vowels_in_dict_keys(dict):
    """
    Given a dictionary, write a function that checks if all the keys are strings in either lower case or upper case 
    and returns a dictionary where keys are the same keys from the input dictionary and the values are the count of vowels in each key. 
    If the keys are not all in lower case nor all in upper case, return an empty dictionary. 
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.
    The function should return an empty dictionary if the input dictionary itself is empty.
    
    Examples:
    vowels_in_dict_keys({"a":"apple", "b":"banana"}) should return {"a":1, "b":0}.
    vowels_in_dict_keys({"a":"apple", "A":"banana", "B":"banana"}) should return {}.
    vowels_in_dict_keys({"a":"apple", 8:"banana", "a":"apple"}) should return {}.
    vowels_in_dict_keys({"Name":"John", "Age":"36", "City":"Houston"}) should return {}.
    vowels_in_dict_keys({"STATE":"NC", "ZIP":"12345" }) should return {"STATE": 2, "ZIP": 1}.
    """
    if not dict:
        return {}
    lowercase_keys = []
    uppercase_keys = []
    for key in dict.keys():
        if isinstance(key, str):
            if key.islower():
                lowercase_keys.append(key)
            elif key.isupper():
                uppercase_keys.append(key)
            else:
                return {}
        else:
            return {}
    result = {}
    for key in lowercase_keys:
        count = 0
        for char in key:
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                count += 1
        result[key] = count
    for key in uppercase_keys:
        count = 0
        for char in key:
            if char.lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
                count += 1
        result[key] = count
    return result