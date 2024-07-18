def prime_length(string, opt=None):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if opt == 'letters':
        count = len(set(string))
    elif opt == 'words':
        count = len([word for word in string.split() if word])
    else:
        count = len(string)
    return is_prime(count)