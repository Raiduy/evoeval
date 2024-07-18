def add(lst, n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_count = sum((is_prime(num) for num in lst))
    if prime_count == 0:
        return -1
    even_sum = sum((num for (i, num) in enumerate(lst) if i % 2 != 0 and num % 2 == 0))
    return even_sum * prime_count