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

    >>> count_uppercase_lowercase('HelloWorld')
    {'uppercase': 2, 'lowercase': 8}
    >>> count_uppercase_lowercase('GoodBye')
    {'uppercase': 2, 'lowercase': 5}
    >>> count_uppercase_lowercase('MorningSun')
    {'uppercase': 2, 'lowercase': 8}
    >>> count_uppercase_lowercase('NightMoon')
    {'uppercase': 2, 'lowercase': 7}
    >>> count_uppercase_lowercase('BadWeather')
    {'uppercase': 2, 'lowercase': 8}
    """
    if not is_valid_input(string):
        return {'uppercase': -1, 'lowercase': -1}
    uppercase_count = sum((1 for char in string if char.isupper()))
    lowercase_count = sum((1 for char in string if char.islower()))
    return {'uppercase': uppercase_count, 'lowercase': lowercase_count}