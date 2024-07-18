def check_for_special_characters(input_string):
    """
    Helper Function:
    Write a function that takes a string, 
    and checks if it has any special characters.
    
    Returns true if it has any special characters, else returns false.
    
    Examples:
    >>> check_for_special_characters('Test123')
    False
    >>> check_for_special_characters('Test@123')
    True
    """
    special_chars = "!@#$%^&*()-+?_=,<>/"
    return any(c in special_chars for c in input_string)
def convert_strings(input_list):
    """
    Write a function that takes a list of strings and converts the strings 
    in the following way:
    1. If the string has any special characters ("!@#$%^&*()-+?_=,<>/"), remove those characters.
    2. If the string has any numbers, replace those numbers with their 
       corresponding english words (e.g., '1' to 'ONE').
    3. Make all the characters in the string uppercase.
    
    Return the converted list of strings.

    Assume each string in the list only contains alphanumeric characters and 
    possible special characters. The list can be empty, but will not contain 
    any non-string elements.

    Examples:
    >>> convert_strings(['test', '123', 'Test@123'])
    ['TEST', 'ONETWOTHREE', 'TESTONETWOTHREE']
    >>> convert_strings(['', 'test1', '2test'])
    ['', 'TESTONE', 'TWOTEST']
    """
    converted_list = []
    for string in input_list:
        converted_string = ''
        for char in string:
            if char.isalpha():
                converted_string += char.upper()
            elif char.isdigit():
                if char == '0':
                    converted_string += 'ZERO'
                elif char == '1':
                    converted_string += 'ONE'
                elif char == '2':
                    converted_string += 'TWO'
                elif char == '3':
                    converted_string += 'THREE'
                elif char == '4':
                    converted_string += 'FOUR'
                elif char == '5':
                    converted_string += 'FIVE'
                elif char == '6':
                    converted_string += 'SIX'
                elif char == '7':
                    converted_string += 'SEVEN'
                elif char == '8':
                    converted_string += 'EIGHT'
                elif char == '9':
                    converted_string += 'NINE'
            elif char.isalnum():
                converted_string += char
        converted_list.append(converted_string)
    return converted_list