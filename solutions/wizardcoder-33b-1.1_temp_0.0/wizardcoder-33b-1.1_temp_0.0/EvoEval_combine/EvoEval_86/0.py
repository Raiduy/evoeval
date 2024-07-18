
def evaluate_common_expressions(operators, operand_lists):
    common_operands = set(operand_lists[0])
    for operand_list in operand_lists[1:]:
        common_operands &= set(operand_list)
    if not common_operands:
        return None
    common_operands = sorted(list(common_operands))
    result = common_operands[0]
    for (i, operator) in enumerate(operators):
        if operator == '+':
            result += common_operands[i + 1]
        elif operator == '-':
            result -= common_operands[i + 1]
        elif operator == '*':
            result *= common_operands[i + 1]
        elif operator == '//':
            result //= common_operands[i + 1]
        elif operator == '**':
            result **= common_operands[i + 1]
    return result