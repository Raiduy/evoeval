
def do_algebra(operator, operand):
    """
    Given two lists 'operator' and 'operand'. The first list 'operator' contains basic algebraic operations,
    and the second list 'operand' is a list of integers. This function is designed to use the two provided lists
    to construct and evaluate an algebraic expression.

    The 'operator' list can contain the following basic algebra operations:
    - Addition ( + ) 
    - Subtraction ( - ) 
    - Multiplication ( * ) 
    - Floor division ( // ) 
    - Exponentiation ( ** ) 

    The function constructs an algebraic expression by applying each operator from the 'operator' list in order
    to the corresponding elements in the 'operand' list, starting from the first element. 

    The function then evaluates this algebraic expression and returns the result.

    Note the following constraints:
    - The length of the 'operator' list is exactly one element less than the length of the 'operand' list. This is because each operator is applied between two operands.
    - 'operand' is a list of non-negative integers. It does not contain any other types of elements.
    - The 'operator' list contains at least one operator, and the 'operand' list contains at least two operands. This is because at least one operation must be performed.

    Example:
    Given:
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    The function constructs and evaluates the algebraic expression: 2 + 3 * 4 - 5
    The function returns: 9

    """
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += ' ' + operator[i] + ' ' + str(operand[i + 1])
    return eval(expression)