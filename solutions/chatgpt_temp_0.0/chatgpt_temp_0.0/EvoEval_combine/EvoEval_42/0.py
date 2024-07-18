
def check_expression(expression: str):
    stack = []
    i = 0
    while i < len(expression):
        if expression[i] == '<':
            stack.append('<')
        elif expression[i] == '>':
            if len(stack) == 0 or stack[-1] != '<':
                return False
            stack.pop()
        elif expression[i] == ',':
            if len(stack) == 0 or stack[-1] != '<':
                return False
        i += 1
    if len(stack) > 0:
        return False
    fractions = expression[1:-1].split(',')
    product = 1
    for fraction in fractions:
        (numerator, denominator) = map(int, fraction.split('/'))
        product *= numerator / denominator
    return product.is_integer()