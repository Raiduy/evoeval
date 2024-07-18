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
    """
    Rearrange the words in input_string according to the order specified in arrangement_order.
    Arrangement_order should be a list of indices.
    The rearrangement should be done such that the word at the index in the original string 
    goes to the corresponding position in the arrangement_order.
    If a word in the input_string is repeated, the function should prioritize the first occurrence 
    of the word for rearranging.
    If arrangement_order contains an index that is not in the input_string, return "Invalid arrangement order"
    
    The function should return the rearranged sentence as a string.
    
    >>> rearrange_words('The quick brown fox jumps over the lazy dog', [8, 7, 0, 1, 2, 3, 4, 5, 6])
    'dog lazy The quick brown fox jumps over the'
    >>> rearrange_words('I love to code in Python', [4, 3, 2, 1, 0])
    'in code to love I'
    """
    words = parse_input(input_string)
    if len(set(arrangement_order)) != len(arrangement_order) or max(arrangement_order) >= len(words):
        return 'Invalid arrangement order'
    return ' '.join([words[i] for i in arrangement_order])