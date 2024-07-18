

def prime_fib(n: int) -> int:
    """
    Returns the n-th Fibonacci number which is also a prime number.
    
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
    fib_num = 0
    while True:
        fib_num += 1
        if is_prime(fib(fib_num)):
            count += 1
            if count == n:
                return fib(fib_num)