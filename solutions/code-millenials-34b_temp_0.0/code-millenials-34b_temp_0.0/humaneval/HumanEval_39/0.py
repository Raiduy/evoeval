

def prime_fib(n):
    i = 1
    while True:
        fib = fibonacci(i)
        if is_prime(fib):
            n -= 1
            if n == 0:
                return fib
        i += 1
