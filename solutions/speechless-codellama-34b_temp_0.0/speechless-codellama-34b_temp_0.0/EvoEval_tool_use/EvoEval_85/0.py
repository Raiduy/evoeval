def is_valid_string(input_string):
    """Check if a given string is valid. 
    A string is valid if it does not contain any special characters (!@#$%^&*()-_+={}[]|\/:;<>,.?).

    Returns True if the string is valid, False otherwise.
    """
    special_chars = "!@#$%^&*()-_+={}[]|\/:;<>,.?"
    for char in input_string:
        if char in special_chars:
            return False
    return True

def is_valid_length(input_string):
    """Check if a given string is of valid length.
    A string is of valid length if it is not empty and has 10 or less characters.

    Returns True if the string is of valid length, False otherwise.
    """
    if len(input_string) == 0 or len(input_string) > 10:
        return False
    return True
def string_processing(input_string):
    """You will be given a string. Your task is to process this string and return a new string.

    The processing should happen in the following manner:
    - If the first character of the string is 'a', add "123" at the end
    - If the first character of the string is 'b', reverse the string
    - If the first character of the string is 'c', replace all 'e's in the string with 'i'
    - If the first character of the string is neither 'a', 'b', nor 'c', return the string as is

    The returned string should be in lowercase.

    Note: For this function to work correctly:
    - The string should not contain any special characters (!@#$%^&*()-_+={}[]|\\/:;<>,.?)
    - The string should be not empty and contain 10 or less characters
    - return "Invalid input string" if it violates the above rules

    Examples:
    string_processing("apple")   # returns "apple123"
    string_processing("Banana")  # returns "ananabb"
    string_processing("celery")  # returns "ciliry"
    string_processing("donut")   # returns "donut"
    """
    if not is_valid_string(input_string) or not is_valid_length(input_string):
        return 'Invalid input string'
    input_string = input_string.lower()
    if input_string[0] == 'a':
        return input_string + '123'
    elif input_string[0] == 'b':
        return input_string[::-1]
    elif input_string[0] == 'c':
        return input_string.replace('e', 'i')
    else:
        return input_string