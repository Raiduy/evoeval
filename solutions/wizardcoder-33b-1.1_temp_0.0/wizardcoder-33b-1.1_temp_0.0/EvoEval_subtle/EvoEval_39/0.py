
def prime_fib(n):
    count = 0
    i = 0
    while count < n:
        i += 1
        fib_num = fib(i)
        if fib_num % 2 != 0 and is_prime(fib_num):
            count += 1
    return fib_num