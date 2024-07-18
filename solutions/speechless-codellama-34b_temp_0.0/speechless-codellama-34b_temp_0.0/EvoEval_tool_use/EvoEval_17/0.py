def validate_string(input_string: str) -> bool:
    valid_chars = ['a', 'b', 'c', ' ', '|']
    for char in input_string:
        if char not in valid_chars:
            return False
    return True
def parse_string(input_string: str) -> str:
    if not validate_string(input_string):
        return 'Invalid input string'
    words = input_string.split()
    parsed_words = []
    for word in words:
        if word == 'a|':
            parsed_words.append('a big apple')
        elif word == 'b|':
            parsed_words.append('a bunch of bananas')
        elif word == 'c|':
            parsed_words.append('a cherry pie')
        elif word == 'a':
            parsed_words.append('apple')
        elif word == 'b':
            parsed_words.append('banana')
        elif word == 'c':
            parsed_words.append('cherry')
    return ', '.join(parsed_words)