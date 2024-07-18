
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime. If the number is even, return None.
    """
    count = 0
    for fib_num in fib_generator():
        if fib_num > 2 and fib_num % 2 == 0:
            continue
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        if count == n:
            break