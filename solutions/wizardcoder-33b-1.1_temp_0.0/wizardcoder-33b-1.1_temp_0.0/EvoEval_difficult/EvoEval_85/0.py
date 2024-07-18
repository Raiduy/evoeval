def add(lst, n):
    total = 0
    prime_count = 0
    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            total += lst[i]
        if is_prime(lst[i]):
            prime_count += 1
    if prime_count == 0:
        return -1
    else:
        return total * prime_count