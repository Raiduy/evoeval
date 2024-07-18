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
    1. If the string has any special characters ("!@#$%^&*()-+?_=,<>/""), remove those characters.
    2. If the string has any numbers, replace those numbers with their 
       corresponding english words (e.g., '1' to 'ONE').
    3. Make all the characters in the string uppercase.
    
    Return the converted list of strings.
    """
    num_dict = {'1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR', '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE', '0': 'ZERO'}
    converted_list = []
    for string in input_list:
        if check_for_special_characters(string):
            string = ''.join((e for e in string if e not in '!@#$%^&*()-+?_=,<>/"'))
        new_string = ''
        for char in string:
            if char.isdigit():
                new_string += num_dict[char]
            else:
                new_string += char
        converted_list.append(new_string.upper())
    return converted_list