
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Ensure the start is always the smaller number
    start, end = sorted([a, b])
    
    # Generate the range of numbers between start and end, inclusive
    numbers = range(start, end + 1)
    
    # Filter out the even numbers and return them
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    return even_numbers
