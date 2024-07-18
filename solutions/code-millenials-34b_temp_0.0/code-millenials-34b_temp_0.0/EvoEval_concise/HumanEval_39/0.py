

def prime_fib(n):
    i = 1
    while True:
        fib_num = fib(i)
        if is_prime(fib_num):
            if n == 1:
                return fib_num
            n -= 1
        i += 1