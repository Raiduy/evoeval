def add(lst, n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_count = sum((1 for num in lst if is_prime(num)))
    if prime_count == 0:
        return -1
    total_sum = sum((lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0))
    return total_sum * prime_count