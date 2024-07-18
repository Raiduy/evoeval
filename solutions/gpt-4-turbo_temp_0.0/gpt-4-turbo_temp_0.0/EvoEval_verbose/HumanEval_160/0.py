
def do_algebra(operator, operand):
    import operator as op
    operator_map = {'+': op.add, '-': op.sub, '*': op.mul, '//': op.floordiv, '**': op.pow}
    result = operand[0]
    for (i, oper) in enumerate(operator):
        operation = operator_map[oper]
        result = operation(result, operand[i + 1])
    return result