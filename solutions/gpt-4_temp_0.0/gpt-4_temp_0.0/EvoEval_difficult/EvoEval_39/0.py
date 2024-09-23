def prime_fib_matrix(n: int, m: int):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fib(n):
        fibs = [0, 1]
        for i in range(2, n + 1):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs
    prime_fibs = [x for x in fib(n * m) if is_prime(x)]
    matrix = [[prime_fibs[i * j] for j in range(m)] for i in range(n)]
    return matrix