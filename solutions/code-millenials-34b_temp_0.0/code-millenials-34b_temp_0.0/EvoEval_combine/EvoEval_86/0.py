
def evaluate_common_expressions(operators, operand_lists):
    common_operands = set(operand_lists[0])
    for operand_list in operand_lists[1:]:
        common_operands = common_operands.intersection(set(operand_list))
    common_operands = sorted(list(common_operands))
    if not common_operands:
        return None
    result = common_operands[0]
    for i in range(1, len(common_operands)):
        if operators[i - 1] == '+':
            result += common_operands[i]
        elif operators[i - 1] == '-':
            result -= common_operands[i]
        elif operators[i - 1] == '*':
            result *= common_operands[i]
        elif operators[i - 1] == '//':
            result //= common_operands[i]
        elif operators[i - 1] == '**':
            result **= common_operands[i]
    return result