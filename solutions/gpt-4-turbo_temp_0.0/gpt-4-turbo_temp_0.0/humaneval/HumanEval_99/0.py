
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.
    '''
    # Convert the string to a floating-point number
    num = float(value)
    
    # Get the decimal part of the number
    decimal_part = num - int(num)
    
    # Check if the number is positive or negative
    if num > 0:
        # For positive numbers, if the decimal part is >= 0.5, round up, else round down
        if decimal_part >= 0.5:
            return int(num) + 1
        else:
            return int(num)
    else:
        # For negative numbers, if the decimal part <= -0.5, round down, else round up
        if decimal_part <= -0.5:
            return int(num) - 1
        else:
            return int(num)
