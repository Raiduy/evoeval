def validate_string(input_string: str) -> bool:
    valid_chars = ['a', 'b', 'c', ' ', '|']
    for char in input_string:
        if char not in valid_chars:
            return False
    return True
def parse_string(input_string: str) -> str:
    legend = {'a': 'apple', 'b': 'banana', 'c': 'cherry', 'a|': 'a big apple', 'b|': 'a bunch of bananas', 'c|': 'a cherry pie'}
    parts = input_string.split()
    result = []
    for part in parts:
        if part in legend:
            result.append(legend[part])
        elif part + '|' in legend:
            result.append(legend[part + '|'])
        else:
            result.append(legend.get(part, ''))
    return ', '.join(result)