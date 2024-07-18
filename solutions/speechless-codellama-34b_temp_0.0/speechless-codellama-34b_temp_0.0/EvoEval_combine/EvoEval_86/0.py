
def evaluate_common_expressions(operators, operand_lists):
    common_operands = set(operand_lists[0])
    for operand_list in operand_lists[1:]:
        common_operands &= set(operand_list)
    if not common_operands:
        return None
    common_operands = sorted(common_operands)
    result = common_operands[0]
    for i in range(1, len(common_operands)):
        operator = operators[i - 1]
        if operator == '+':
            result += common_operands[i]
        elif operator == '-':
            result -= common_operands[i]
        elif operator == '*':
            result *= common_operands[i]
        elif operator == '//':
            result //= common_operands[i]
        elif operator == '**':
            result **= common_operands[i]
    return result