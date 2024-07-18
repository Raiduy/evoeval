def prime_length(string, opt=None):
    """Return True if the count of unique letters, words, or length of the string is prime."""
    if opt == 'letters':
        count = len(set(string))
    elif opt == 'words':
        words = string.replace(',', ' ').split()
        count = len(words)
    else:
        count = len(string)
    return is_prime(count)