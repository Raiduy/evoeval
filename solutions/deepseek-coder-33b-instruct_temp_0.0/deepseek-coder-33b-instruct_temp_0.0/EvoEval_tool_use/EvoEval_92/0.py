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
    num_to_word = {'0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR', '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'}
    special_chars = '!@#$%^&*()-+?_=,<>/'
    converted_list = []
    for s in input_list:
        s = ''.join((c for c in s if c not in special_chars))
        s = ''.join((num_to_word[c] if c.isdigit() else c for c in s))
        s = s.upper()
        converted_list.append(s)
    return converted_list