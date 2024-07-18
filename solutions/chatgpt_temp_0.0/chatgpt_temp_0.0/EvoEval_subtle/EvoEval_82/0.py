
def prime_length(string):
    string = string.replace(' ', '')
    length = len(string)
    if length < 2:
        return False
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return False
    return True