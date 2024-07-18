
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Function to convert input to float, handling commas as decimal points
    def to_float(x):
        if isinstance(x, str):
            x = x.replace(',', '.')
        return float(x)
    
    # Convert both inputs to floats for comparison
    a_float = to_float(a)
    b_float = to_float(b)
    
    # Compare the float representations
    if a_float > b_float:
        return a
    elif b_float > a_float:
        return b
    else:
        return None
