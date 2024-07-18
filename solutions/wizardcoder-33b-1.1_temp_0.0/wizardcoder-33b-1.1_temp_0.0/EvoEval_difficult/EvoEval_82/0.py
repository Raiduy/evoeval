def prime_length(string, opt=None):
    if opt == 'letters':
        return is_prime(len(set(string)))
    elif opt == 'words':
        return is_prime(len([word for word in string.split() if word]))
    else:
        return is_prime(len(string))