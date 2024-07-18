def prime_fib_matrix(n: int, m: int):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(n):
        if n < 2:
            return n
        (a, b) = (0, 1)
        for _ in range(n - 1):
            (a, b) = (b, a + b)
        return b
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            k = i * j + 1
            while True:
                fib = fibonacci(k)
                if is_prime(fib):
                    row.append(fib)
                    break
                k += 1
        result.append(row)
    return result