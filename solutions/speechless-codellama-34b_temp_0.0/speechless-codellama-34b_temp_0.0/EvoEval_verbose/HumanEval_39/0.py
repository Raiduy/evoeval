

def prime_fib(n: int) -> int:
    """
    Calculates the nth number that is both a Fibonacci number and a prime number.
    """
    count = 0
    i = 0
    while count < n:
        fib = fibonacci(i)
        if is_prime(fib):
            count += 1
        i += 1
    return fibonacci(i - 1)