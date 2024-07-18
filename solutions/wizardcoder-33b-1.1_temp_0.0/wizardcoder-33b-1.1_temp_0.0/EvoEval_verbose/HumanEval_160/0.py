
def do_algebra(operator, operand):
    operator_dict = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '//': lambda x, y: x // y, '**': lambda x, y: x ** y}
    result = operand[0]
    for i in range(1, len(operand)):
        result = operator_dict[operator[i - 1]](result, operand[i])
    return result