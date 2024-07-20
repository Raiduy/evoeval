
def check_expression(expression: str) -> bool:
    import re
    from fractions import Fraction
    expressions = re.findall('<(.*?)>', expression)
    if expression.count('<') != expression.count('>'):
        return False
    for expr in expressions:
        fractions = expr.split(',')
        product = 1
        for fraction in fractions:
            (numerator, denominator) = map(int, fraction.split('/'))
            product *= Fraction(numerator, denominator)
        if product.denominator != 1:
            return False
    return True