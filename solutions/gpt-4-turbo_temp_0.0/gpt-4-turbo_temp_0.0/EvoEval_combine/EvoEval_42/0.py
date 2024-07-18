
def check_expression(expression: str) -> bool:
    expressions = expression.split('><')
    if expressions[0][0] != '<' or expressions[-1][-1] != '>':
        return False
    for (i, expr) in enumerate(expressions):
        if i == 0 and expr[-1] != '>':
            expr += '>'
        elif i == len(expressions) - 1 and expr[0] != '<':
            expr = '<' + expr
        elif i != 0 and i != len(expressions) - 1:
            expr = '<' + expr + '>'
        fractions = expr[1:-1].split(',')
        product = 1
        for fraction in fractions:
            (numerator, denominator) = map(int, fraction.split('/'))
            product *= numerator / denominator
        if product % 1 != 0:
            return False
    return True