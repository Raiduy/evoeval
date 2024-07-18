
def prime_length(string):
    """Return True if the length of the string is a prime number, False otherwise."""
    string = string.replace(' ', '')
    return is_prime(len(string))