def parse_pairs(text):
    """parse_pairs is a helper function that separates the text into pairs of words.
    It returns a list of tuples where each tuple is a pair of words.

    >>> parse_pairs('apple fruit, banana fruit, apple tech, banana tech')
    [('apple', 'fruit'), ('banana', 'fruit'), ('apple', 'tech'), ('banana', 'tech')]

    >>> parse_pairs('red color, blue color')
    [('red', 'color'), ('blue', 'color')]

    >>> parse_pairs('cat animal, dog animal, bird animal')
    [('cat', 'animal'), ('dog', 'animal'), ('bird', 'animal')]

    >>> parse_pairs('python programming, java programming, python snake')
    [('python', 'programming'), ('java', 'programming'), ('python', 'snake')]
    """
    pairs = text.split(', ')
    return [tuple(pair.split(' ')) for pair in pairs]
def text_to_dict(text: str):
    """text_to_dict is a function that takes a string of text containing pairs of
    words separated by commas and converts each pair into a key-value pair in a dictionary.
    Each pair of words in the text is separated by a space and every two pairs are separated by a comma. 
    If a word appears more than once as a key, the value for that key should be a list of all the 
    corresponding values in the order they appeared in the text.

    >>> text_to_dict('apple fruit, banana fruit, apple tech, banana tech')
    {'apple': ['fruit', 'tech'], 'banana': ['fruit', 'tech']}

    >>> text_to_dict('red color, blue color')
    {'red': 'color', 'blue': 'color'}

    >>> text_to_dict('cat animal, dog animal, bird animal')
    {'cat': 'animal', 'dog': 'animal', 'bird': 'animal'}

    >>> text_to_dict('python programming, java programming, python snake')
    {'python': ['programming', 'snake'], 'java': 'programming'}
    """
    pairs = parse_pairs(text)
    result_dict = {}
    for (key, value) in pairs:
        if key in result_dict:
            if isinstance(result_dict[key], list):
                result_dict[key].append(value)
            else:
                result_dict[key] = [result_dict[key], value]
        else:
            result_dict[key] = value
    return result_dict