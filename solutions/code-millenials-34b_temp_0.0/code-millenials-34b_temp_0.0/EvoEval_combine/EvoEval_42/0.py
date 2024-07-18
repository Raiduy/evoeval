
def check_expression(expression: str):
    stack = []
    fractions = expression.split('>')
    for fraction in fractions:
        if fraction.count('<') != fraction.count(','):
            return False
    for fraction in fractions:
        fraction = fraction.replace('<', '')
        fraction = fraction.replace(' ', '')
        if fraction:
            nums = fraction.split(',')
            product = 1
            for num in nums:
                (a, b) = map(int, num.split('/'))
                product *= a / b
            if not product.is_integer():
                return False
    return True