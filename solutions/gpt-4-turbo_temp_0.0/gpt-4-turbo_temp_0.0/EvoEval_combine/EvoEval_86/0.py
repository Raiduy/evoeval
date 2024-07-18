
def evaluate_common_expressions(operators, operand_lists):
    common_operands = set(operand_lists[0])
    for operand_list in operand_lists[1:]:
        common_operands.intersection_update(operand_list)
    common_operands = sorted(common_operands)
    if not common_operands:
        return None
    expression = str(common_operands[0])
    for (i, operand) in enumerate(common_operands[1:]):
        if i < len(operators):
            expression += f' {operators[i]} {operand}'
        else:
            break
    result = eval(expression)
    return result