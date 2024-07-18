
def prime_fib(n: int) -> int:
    if n < 1:
        return None
    fib = [0, 1]
    count = 0
    while count < n:
        fib.append(fib[-1] + fib[-2])
        if is_prime(fib[-1]) and fib[-1] % 2 != 0:
            count += 1
    return fib[-1]