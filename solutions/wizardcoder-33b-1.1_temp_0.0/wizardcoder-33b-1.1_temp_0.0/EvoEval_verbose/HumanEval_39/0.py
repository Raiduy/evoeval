

def prime_fib(n: int):

    def fibonacci():
        (a, b) = (0, 1)
        while True:
            yield a
            (a, b) = (b, a + b)

    def primes(n):
        sieve = [True] * n
        for x in range(2, int(n ** 0.5) + 1):
            if sieve[x]:
                for i in range(x * x, n, x):
                    sieve[i] = False
        return [x for x in range(2, n) if sieve[x]]
    fib = fibonacci()
    prime = primes(10000)
    count = 0
    while True:
        f = next(fib)
        if f in prime:
            count += 1
            if count == n:
                return f