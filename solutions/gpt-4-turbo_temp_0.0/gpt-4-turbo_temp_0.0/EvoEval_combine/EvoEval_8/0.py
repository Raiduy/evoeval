
def correct_bracket_sequence_and_count(string: str, bracket: str) -> tuple:
    """
    This function checks if a given string has correctly paired opening and closing brackets and 
    counts how many times a specific bracket appears in the string, including overlapping cases.
    
    The function takes a string of "<" and ">" characters and a specific bracket ("<" or ">") 
    as inputs, and returns a tuple with a boolean value and an integer. The boolean value represents 
    whether every opening bracket has a corresponding closing bracket. The integer represents the 
    count of the specific bracket in the string.

    >>> correct_bracket_sequence_and_count('<<><>>', '<')
    (True, 3)
    >>> correct_bracket_sequence_and_count('<<><>>', '>')
    (True, 3)
    >>> correct_bracket_sequence_and_count('<>', '<')
    (True, 1)
    >>> correct_bracket_sequence_and_count('><<>', '>')
    (False, 2)
    >>> correct_bracket_sequence_and_count('', '>')
    (True, 0)
    """
    open_brackets = 0
    bracket_count = 0
    for char in string:
        if char == bracket:
            bracket_count += 1
        if char == '<':
            open_brackets += 1
        elif char == '>':
            open_brackets -= 1
        if open_brackets < 0:
            return (False, bracket_count)
    return (open_brackets == 0, bracket_count)