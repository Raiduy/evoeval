
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # Initialize an empty list to store the numbers with no even digits
    no_even_digits = []

    # Iterate over the list of numbers
    for num in x:
        # Convert the number to a string to be able to iterate over its digits
        str_num = str(num)
        # Check if the number has any even digit
        if all(int(digit) % 2 != 0 for digit in str_num):
            # If the number has no even digit, add it to the list
            no_even_digits.append(num)

    # Sort the list in increasing order and return it
    return sorted(no_even_digits)
