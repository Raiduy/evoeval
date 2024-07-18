def validate_input(input_dict):
    """
    This is a helper function which is used to validate the input dictionary. 
    It takes a dictionary as an input and returns True if all the keys in the 
    dictionary are strings and all the values are integers, otherwise returns False.
    """
    for key, value in input_dict.items():
        if not isinstance(key, str):
            return False
        if not isinstance(value, int):
            return False
    return True
def find_maximum(input_dict):
    """
    Write a function that takes a dictionary where keys are strings and values are integers.
    This function should return a tuple with the string(key) that has the highest integer(value) 
    along with the maximum integer. If the dictionary is empty, return an empty dictionary.
    If the dictionary does contain all string as keys and integer as values, return "Invalid input"
    Note: you may assume all strings are different and the input dictionary will not contain 
    duplicate values.
    """
    if not input_dict:
        return {}
    if not validate_input(input_dict):
        return 'Invalid input'
    max_key = max(input_dict, key=input_dict.get)
    max_value = input_dict[max_key]
    return (max_key, max_value)