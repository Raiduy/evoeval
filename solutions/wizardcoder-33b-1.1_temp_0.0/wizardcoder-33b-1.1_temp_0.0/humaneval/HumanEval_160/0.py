
def do_algebra(operator, operand):
    # Create a string of the algebraic expression
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += ' ' + operator[i] + ' ' + str(operand[i+1])

    # Evaluate the expression and return the result
    return eval(expression)
