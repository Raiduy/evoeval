
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise. The function should ignore white spaces in the string length calculation."""
    length_without_spaces = len(string.replace(' ', ''))
    return is_prime(length_without_spaces)