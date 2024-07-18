def prime_length(string, opt):
    if opt == 'letters':
        unique_letters = set(string)
        count = len(unique_letters)
    elif opt == 'words':
        words = [word for word in string.replace(',', ' ').split() if word]
        count = len(words)
    else:
        count = len(string)
    return is_prime(count)