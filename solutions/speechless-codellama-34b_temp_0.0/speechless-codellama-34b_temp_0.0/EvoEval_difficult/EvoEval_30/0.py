def get_positive_and_index(l: list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for (i, num) in enumerate(l):
        if num > 0 and is_prime(i):
            result.append((num, i))
    return result