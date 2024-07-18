
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime. If the number is even, return None.
    >>> prime_fib(1)
    None
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    if n < 1:
        return None
    fib_sequence = [0, 1]
    while len(fib_sequence) < n + 1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    for num in fib_sequence:
        if num % 2 == 0:
            return None
        if is_prime(num):
            n -= 1
            if n == 0:
                return num