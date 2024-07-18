

def prime_fib(n):
    (a, b) = (0, 1)
    count = 0
    while count < n:
        (a, b) = (b, a + b)
        if is_prime(b):
            count += 1
    return b