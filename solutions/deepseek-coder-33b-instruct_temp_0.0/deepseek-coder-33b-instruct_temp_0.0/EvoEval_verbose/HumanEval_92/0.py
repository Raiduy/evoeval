
def any_int(x, y, z):
    """
    This function named 'any_int' takes three input arguments, all of which are numbers. These input arguments are denoted as x, y, and z. 

    The function performs a specific calculation to determine whether one of the numbers equals the sum of the other two numbers. In order for this function to return 'True', two conditions must be met. 

    First, one of the input numbers must equate to the sum of the other two. For instance, if the inputs are 5, 2, and 7, the function returns 'True' because 5+2 equals 7. The order of the numbers does not matter. 

    Secondly, all input numbers must be integers. In Python, integers are whole numbers without a decimal point. For example, 3 and -2 are integers, but 3.6 and -2.2 are not. 

    If either of the conditions is not met, the function will return 'False'. For instance, when the inputs are 3, 2, and 2, the function returns 'False' because none of the numbers equals the sum of the other two. Similarly, if any of the inputs are not integers (e.g., 3.6, -2.2, 2), the function returns 'False'. 

    Here are some examples of how to call this function and what it returns:
    
    Example 1: any_int(5, 2, 7)
    This returns 'True' because 5+2 equals 7 and all numbers are integers.

    Example 2: any_int(3, 2, 2)
    This returns 'False' because no number equals the sum of the other two, even though all numbers are integers.

    Example 3: any_int(3, -2, 1)
    This returns 'True' because 3+(-2) equals 1 and all numbers are integers.

    Example 4: any_int(3.6, -2.2, 2)
    This returns 'False' because not all numbers are integers, despite the fact that 3.6+(-2.2) equals 2.
    
    """
    if not all((isinstance(i, int) for i in [x, y, z])):
        return False
    if x + y == z or x + z == y or y + z == x:
        return True
    return False