

def prime_fib(n: int):
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

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    fib_nums = [0, 1]
    count = 0
    i = 1
    while count < n:
        fib_nums.append(fib_nums[i] + fib_nums[i - 1])
        if is_prime(fib_nums[-1]):
            count += 1
        i += 1
    return fib_nums[-1]