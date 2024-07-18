def add(lst, n):
    even_sum = 0
    prime_count = 0
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_sum += lst[i]
        if is_prime(lst[i]):
            prime_count += 1
    if prime_count == 0:
        return -1
    return even_sum * prime_count