
def check_expression(expression: str):
    if not expression.startswith('<') or not expression.endswith('>'):
        return False
    expression = expression[1:-1]
    fractions = expression.split(',')
    product = 1
    for fraction in fractions:
        (numerator, denominator) = map(int, fraction.split('/'))
        product *= numerator / denominator
    return product.is_integer()