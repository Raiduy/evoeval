def validate_string(input_string: str) -> bool:
    valid_chars = ['a', 'b', 'c', ' ', '|']
    for char in input_string:
        if char not in valid_chars:
            return False
    return True
def parse_string(input_string: str) -> str:
    if not validate_string(input_string):
        raise ValueError('Invalid input string')
    legend = {'a': 'apple', 'b': 'banana', 'c': 'cherry', 'a|': 'a big apple', 'b|': 'a bunch of bananas', 'c|': 'a cherry pie'}
    words = input_string.split()
    result = []
    for word in words:
        result.append(legend[word])
    return ', '.join(result)