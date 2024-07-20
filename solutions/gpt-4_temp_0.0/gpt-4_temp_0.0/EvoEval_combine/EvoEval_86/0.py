
def evaluate_common_expressions(operators, operand_lists):
    common_operands = list(set.intersection(*map(set, operand_lists)))
    common_operands.sort()
    if not common_operands:
        return None
    expression = str(common_operands[0])
    for i in range(1, len(common_operands)):
        expression += ' ' + operators[i - 1] + ' ' + str(common_operands[i])
    return eval(expression)