def is_valid_input(string):
    """
    A function to validate if the given input string consists of only alphanumeric characters.
    
    :param string: A string value
    :return: True if the string contains only alphanumeric characters, False otherwise
    """
    if string.isalnum():
        return True
    return False
def count_uppercase_lowercase(string):
    if not is_valid_input(string):
        return {'uppercase': -1, 'lowercase': -1}
    uppercase_count = sum((1 for char in string if char.isupper()))
    lowercase_count = sum((1 for char in string if char.islower()))
    return {'uppercase': uppercase_count, 'lowercase': lowercase_count}