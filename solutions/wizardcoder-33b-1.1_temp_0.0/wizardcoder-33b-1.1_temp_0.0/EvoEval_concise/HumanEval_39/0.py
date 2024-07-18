

def prime_fib(n):
    i = 1
    count = 0
    while True:
        fib_num = fib(i)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        i += 1