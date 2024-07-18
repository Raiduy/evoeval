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
    """
    A function to count the number of uppercase and lowercase characters in the given string.

    If non-alphanumeric characters exist in the input, sets the count of uppercase and lowercase to -1 in the output.

    :param string: A string value
    :return: A dictionary with two keys 'uppercase' and 'lowercase', containing the count of uppercase and lowercase characters respectively.
    """
    if not is_valid_input(string):
        return {'uppercase': -1, 'lowercase': -1}
    uppercase_count = 0
    lowercase_count = 0
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return {'uppercase': uppercase_count, 'lowercase': lowercase_count}