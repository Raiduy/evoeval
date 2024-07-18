
def iscube(a):
    """
    The purpose of this function is to determine if a given integer ('a') is a perfect cube of another integer.
    
    This function accepts one input argument:
    a (int): An integer value for which the function will determine if it is a cube root of another integer. 
             The input can be positive, negative, or zero. 

    The function will return a boolean value:
    - It returns True if the input integer is a perfect cube of another integer.
    - It returns False if the input integer is not a perfect cube of another integer.

    Please, note that the function always assumes valid input, hence there is no error/exception handling
    implemented for invalid input scenarios.

    Here are some examples to demonstrate how this function works:

    If the function is called with 1 as the argument (i.e., iscube(1)), it will return True because 1 is a cube of 1.

    If the function is called with 2 as the argument (i.e., iscube(2)), it will return False because 2 is not a cube of any integer.

    If the function is called with -1 as the argument (i.e., iscube(-1)), it will return True because -1 is a cube of -1.

    If the function is called with 64 as the argument (i.e., iscube(64)), it will return True because 64 is a cube of 4.

    If the function is called with 0 as the argument (i.e., iscube(0)), it will return True because 0 is a cube of 0.

    If the function is called with 180 as the argument (i.e., iscube(180)), it will return False because 180 is not a cube of any integer.

    """
    return round(a ** (1.0 / 3)) ** 3 == a