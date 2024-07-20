

def prime_fib(n: int) -> int:
    if n <= 0:
        raise ValueError('n must be a positive integer')
    fib_nums = [0, 1]
    prime_fibs = []
    i = 2
    while len(prime_fibs) < n:
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
        if is_prime(fib_nums[i]):
            prime_fibs.append(fib_nums[i])
        i += 1
    return prime_fibs[n - 1]