
def prime_length(string):
    length = len(string)
    if length < 2:
        return False
    if length == 2 or length == 3:
        return True
    if length % 2 == 0 or length % 3 == 0:
        return False
    i = 5
    while i * i <= length:
        if length % i == 0 or length % (i + 2) == 0:
            return False
        i += 6
    return True