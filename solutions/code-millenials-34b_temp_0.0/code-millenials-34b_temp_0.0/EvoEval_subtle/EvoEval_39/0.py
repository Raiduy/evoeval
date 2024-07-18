
def prime_fib(n):
    i = 0
    while True:
        fib_num = fib(i)
        if is_prime(fib_num):
            n -= 1
            if n == 0:
                return fib_num
        i += 1
    return None