

def prime_fib(n: int) -> int:
    """
    Returns the n-th Fibonacci number which is also a prime number.
    """
    fib_nums = [0, 1]
    count = 0
    while count < n:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
        if is_prime(fib_nums[-1]):
            count += 1
    return fib_nums[-1]