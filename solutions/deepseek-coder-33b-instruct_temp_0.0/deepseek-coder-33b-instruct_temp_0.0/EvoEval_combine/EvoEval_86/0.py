
def evaluate_common_expressions(operators, operand_lists):
    common_operands = set(operand_lists[0]).intersection(*operand_lists)
    common_operands = sorted(list(common_operands))
    if not common_operands:
        return None
    expression = str(common_operands[0])
    for i in range(1, len(common_operands)):
        expression += ' ' + operators[i - 1] + ' ' + str(common_operands[i])
    return eval(expression)