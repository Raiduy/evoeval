def prime_length(string, opt=None):
    if opt == 'letters':
        return is_prime(len(set(string)))
    elif opt == 'words':
        words = string.replace(',', ' ').split()
        return is_prime(len(words))
    elif opt is None:
        return is_prime(len(string))
    else:
        return False