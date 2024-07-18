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
    """
    Evaluates an expression in a custom markup language. The language has two types of elements: strings, which are enclosed 
    in square brackets like "[Hello World]", and numbers, which are enclosed in angle brackets like "<123>". An expression is 
    a sequence of strings and numbers, like "[Hello World]<123>".

    This function should parse the expression and return a new string where each string element is repeated a number of times 
    equal to the next number element in sequence. If a string element is not directly followed by a number, it should be ignored.

    >>> evaluate_expression("[Hello]<3>[World]<2>")
    "HelloHelloHelloWorldWorld"

    >>> evaluate_expression("[Python]<1>[Code]<0>")
    "Python"
    """
    result = ''
    i = 0
    while i < len(expression):
        if expression[i] == '[':
            end_idx = expression.find(']', i)
            if end_idx != -1:
                current_string = parse_string(expression[i:end_idx + 1])
                i = end_idx + 1
                if i < len(expression) and expression[i] == '<':
                    end_num_idx = expression.find('>', i)
                    if end_num_idx != -1:
                        repeat_times = parse_number(expression[i:end_num_idx + 1])
                        result += current_string * repeat_times
                        i = end_num_idx + 1
                        continue
        i += 1
    return result