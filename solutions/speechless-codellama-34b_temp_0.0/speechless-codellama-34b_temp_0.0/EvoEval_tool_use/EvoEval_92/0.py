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
    converted_list = []
    for string in input_list:
        if check_for_special_characters(string):
            string = ''.join((e for e in string if e.isalnum()))
        converted_string = ''.join((str(int(i)) if i.isdigit() else i for i in string))
        converted_string = converted_string.upper()
        converted_list.append(converted_string)
    return converted_list