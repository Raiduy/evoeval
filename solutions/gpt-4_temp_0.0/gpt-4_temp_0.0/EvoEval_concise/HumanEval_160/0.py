
def do_algebra(operator, operand):
    """
    Takes two lists: 'operator', containing basic algebra operations, and 'operand', containing integers. Constructs an algebraic expression using these lists and returns its evaluation.

    Basic algebra operations include:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    Resulting expression: 2 + 3 * 4 - 5
    Output: 9

    Constraints:
    - The length of 'operator' is one less than the length of 'operand'.
    - 'operand' contains non-negative integers only.
    - Both lists are non-empty, with 'operand' containing at least two numbers.
    """
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += ' ' + operator[i] + ' ' + str(operand[i + 1])
    return eval(expression)