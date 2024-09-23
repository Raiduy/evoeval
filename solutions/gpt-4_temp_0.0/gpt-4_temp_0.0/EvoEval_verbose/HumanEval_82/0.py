
def prime_length(string):
    """
    This function checks if the length of the input string is a prime number.
    """
    length = len(string)
    if length < 2:
        return False
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return False
    return True