
def check_expression(expression: str) -> bool:
    fractions = expression.split(',')
    open_brackets = 0
    product = 1
    for fraction in fractions:
        if not fraction.startswith('<') or not fraction.endswith('>'):
            return False
        (numerator, denominator) = fraction[1:-1].split('/')
        if not numerator.isdigit() or not denominator.isdigit():
            return False
        if fraction.startswith('<'):
            open_brackets += 1
        product *= int(numerator) // int(denominator)
    if open_brackets != fractions.count('>'):
        return False
    if product.is_integer():
        return True
    else:
        return False