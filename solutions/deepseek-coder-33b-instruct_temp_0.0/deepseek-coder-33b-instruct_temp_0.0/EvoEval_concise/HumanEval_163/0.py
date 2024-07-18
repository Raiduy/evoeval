
def generate_integers(a, b):
    """
    Returns the even numbers between two positive integers a and b in ascending order, irrespective of the order of a and b. If there are no even numbers, an empty list is returned.
    
    Example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        (a, b) = (b, a)
    return [i for i in range(a, b + 1) if i % 2 == 0]