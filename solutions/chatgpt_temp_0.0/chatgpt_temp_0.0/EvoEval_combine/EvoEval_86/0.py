
def evaluate_common_expressions(operators, operand_lists):
    common_operands = set(operand_lists[0])
    for operand_list in operand_lists[1:]:
        common_operands.intersection_update(operand_list)
    if len(common_operands) == 0:
        return None
    common_operands = sorted(common_operands)
    expression = str(common_operands[0])
    for i in range(1, len(common_operands)):
        expression += ' ' + operators[i - 1] + ' ' + str(common_operands[i])
    return eval(expression)