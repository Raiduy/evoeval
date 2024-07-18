def replace_spaces_with_underscore(string):
    """
    This function receives a string as input and replaces all the spaces in the string with the underscore character (_).
    """
    return string.replace(' ', '_')

def validate_input(string, n):
    """
    This function receives a string and an integer as input and validates them. If the string is empty, it returns 'String is empty'. 
    If n is less than or equal to zero, it returns 'Invalid integer'. Otherwise, it returns 'Valid'.
    """
    if not string:
        return 'String is empty'
    elif n <= 0:
        return 'Invalid integer'
    else:
        return 'Valid'
def replicate_string(string, n):
    """
    Given a string and an integer n, return a new string which is n repetitions of the original string, , with each repetition separated by an underscore.
    If the string is empty, return 'String is empty'. If n is less than or equal to zero, return 'Invalid integer'.

    All spaces in the string should be replaced with the underscore character (_).

    Examples:
    replicate_string("abc", 3) should return "abc_abc_abc".
    replicate_string("abc def", 2) should return "abc_def_abc_def".
    replicate_string("", 2) should return "String is empty".
    replicate_string("abc", 0) should return "Invalid integer".
    replicate_string("abc def ghi", 1) should return "abc_def_ghi".
    """
    validation_result = validate_input(string, n)
    if validation_result != 'Valid':
        return validation_result
    string_with_underscores = replace_spaces_with_underscore(string)
    return '_'.join([string_with_underscores] * n)