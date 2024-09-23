

def prime_fib(n: int) -> int:
    i = count = 0
    while count < n:
        i += 1
        if is_prime(fib(i)):
            count += 1
    return fib(i)