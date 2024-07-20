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
    pairs = parse_pairs(text)
    result = {}
    for pair in pairs:
        (key, value) = pair
        if key in result:
            if type(result[key]) is list:
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value
    return result