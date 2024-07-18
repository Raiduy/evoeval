

def prime_fib(n: int) -> int:
    fib = [0, 1]
    count = 0
    while count < n:
        fib.append(fib[-1] + fib[-2])
        if is_prime(fib[-1]):
            count += 1
    return fib[-1]
