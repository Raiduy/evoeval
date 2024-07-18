
def do_algebra(operator, operand):
    assert len(operator) == len(operand) - 1, 'Length of operator must be one less than length of operand'
    assert all((isinstance(x, int) and x >= 0 for x in operand)), 'All operands must be non-negative integers'
    assert len(operand) >= 2, 'Operand must contain at least two numbers'
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += ' ' + operator[i] + ' ' + str(operand[i + 1])
    result = eval(expression)
    return result