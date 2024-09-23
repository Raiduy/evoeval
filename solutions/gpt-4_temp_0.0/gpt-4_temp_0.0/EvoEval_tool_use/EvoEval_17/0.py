def validate_string(input_string: str) -> bool:
    valid_chars = ['a', 'b', 'c', ' ', '|']
    for char in input_string:
        if char not in valid_chars:
            return False
    return True
def parse_string(input_string: str) -> str:
    legend = {'a': 'apple', 'b': 'banana', 'c': 'cherry', 'a|': 'a big apple', 'b|': 'a bunch of bananas', 'c|': 'a cherry pie'}
    words = input_string.split(' ')
    parsed_words = []
    for word in words:
        if word in legend:
            parsed_words.append(legend[word])
    return ', '.join(parsed_words)