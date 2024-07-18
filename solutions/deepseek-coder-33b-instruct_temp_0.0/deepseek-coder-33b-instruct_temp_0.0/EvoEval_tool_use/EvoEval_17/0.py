def validate_string(input_string: str) -> bool:
    valid_chars = ['a', 'b', 'c', ' ', '|']
    for char in input_string:
        if char not in valid_chars:
            return False
    return True
def parse_string(input_string: str) -> str:
    """
    Input to this function is a string that represents a certain code. This code consists of letters and a '|'
    special character. Each letter and the special character represent a specific word. Letters without the special
    character represent a single word, while letters with the '|' character represent a phrase. 
    Your task is to parse this string and return the corresponding words or phrases. 

    Here is a legend:
    'a' - represents the word "apple"
    'b' - represents the word "banana"
    'c' - represents the word "cherry"
    'a|' - represents the phrase "a big apple"
    'b|' - represents the phrase "a bunch of bananas"
    'c|' - represents the phrase "a cherry pie"

    >>> parse_string('a b| c')
    "apple, a bunch of bananas, cherry"
    >>> parse_string('a| b c|')
    "a big apple, banana, a cherry pie"
    """
    legend = {'a': 'apple', 'b': 'banana', 'c': 'cherry', 'a|': 'a big apple', 'b|': 'a bunch of bananas', 'c|': 'a cherry pie'}
    words = input_string.split()
    parsed_words = [legend[word] for word in words]
    return ', '.join(parsed_words)