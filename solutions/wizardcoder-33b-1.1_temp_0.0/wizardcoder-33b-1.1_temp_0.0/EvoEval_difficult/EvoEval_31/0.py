def is_prime_sum(lst, n):
    prime_set = set()
    for num in lst:
        if is_prime(num):
            prime_set.add(num)
        if n - num in prime_set:
            return True
    return False