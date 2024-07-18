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
            string_start = i + 1
            string_end = expression.find(']', string_start)
            if string_end != -1:
                string_element = parse_string(expression[string_start:string_end])
                i = string_end + 1
                if i < len(expression) and expression[i] == '<':
                    number_start = i + 1
                    number_end = expression.find('>', number_start)
                    if number_end != -1:
                        number_element = parse_number(expression[number_start:number_end])
                        result += string_element * number_element
                        i = number_end + 1
                    else:
                        i = len(expression)
                else:
                    result += string_element
            else:
                i = len(expression)
        else:
            i += 1
    return result