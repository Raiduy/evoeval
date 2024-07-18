

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    count = 0
    for fib_num in fib_generator():
        if fib_num > 1 and is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
