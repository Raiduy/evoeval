
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebraic 
    expression and return the evaluation of this expression.
    """
    # Start with the first operand
    expression = str(operand[0])
    
    # Loop through the operator list and append each operator and the next operand to the expression string
    for i, op in enumerate(operator):
        expression += f" {op} {operand[i+1]}"
    
    # Evaluate the constructed expression string
    result = eval(expression)
    
    return result
