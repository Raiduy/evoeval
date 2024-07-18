
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    """
    
    result = []
    
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            result.append(num)
            
    return sorted(result)

