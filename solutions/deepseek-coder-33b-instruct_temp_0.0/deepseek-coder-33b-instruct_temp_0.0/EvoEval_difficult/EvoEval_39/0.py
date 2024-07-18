def prime_fib_matrix(n: int, m: int):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(n):
        (a, b) = (0, 1)
        for _ in range(n):
            (a, b) = (b, a + b)
        return a
    prime_fib_numbers = [i for i in range(2, 100) if is_prime(i) and is_prime(fibonacci(i))]
    matrix = []
    for i in range(m):
        row = []
        for j in range(m):
            n = i * j
            if n < len(prime_fib_numbers):
                row.append(prime_fib_numbers[n])
            else:
                row.append(-1)
        matrix.append(row)
    return matrix