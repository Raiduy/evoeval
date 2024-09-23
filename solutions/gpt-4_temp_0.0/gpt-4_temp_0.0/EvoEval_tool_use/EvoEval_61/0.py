def parse_string(input_string: str) -> str:
    """
    Helper function to parse a string from our custom markup language, which uses square brackets to denote a string.
    For example, "[Hello World]" should return "Hello World". Assumes well-formed input.
    """
    return input_string[1:-1]

def parse_number(input_string: str) -> int:
    """
    Helper function to parse a number from our custom markup language, which uses angle brackets to denote a number.
    For example, "<123>" should return 123. Assumes well-formed input.
    """
    return int(input_string[1:-1])

def evaluate_expression(expression: str) -> str:
    elements = re.findall('\\[.*?\\]|<.*?>', expression)
    result = ''
    for i in range(len(elements) - 1):
        if elements[i].startswith('[') and elements[i + 1].startswith('<'):
            result += parse_string(elements[i]) * parse_number(elements[i + 1])
    return result