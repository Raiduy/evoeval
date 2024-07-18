

def prime_fib(n: int) -> int:
    """
    The function prime_fib calculates the nth number that is both a Fibonacci number and a prime number.
    """
    count = 0
    fib_index = 1
    while True:
        current_fib = fib(fib_index)
        if is_prime(current_fib):
            count += 1
            if count == n:
                return current_fib
        fib_index += 1