def parse_input(input_string):
    """
    Helper function to parse the input string and return a list of words.
    The input_string should be a sentence where each word is separated by a space.
    If the input_string is not valid (not a string or empty), an error should be raised.
    """
    if not isinstance(input_string, str) or not input_string:
        raise ValueError("Invalid input. Please enter a valid string.")
    return input_string.split()
def rearrange_words(input_string, arrangement_order):
    words = parse_input(input_string)
    rearranged_words = []
    for i in arrangement_order:
        if i < len(words):
            rearranged_words.append(words[i])
        else:
            return 'Invalid arrangement order'
    return ' '.join(rearranged_words)