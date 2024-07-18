def prime_fib_matrix(n: int, m: int):
    matrix = [[0] * m for _ in range(n)]
    fib = list(fibonacci(100))
    k = 0
    for i in range(n):
        for j in range(m):
            while not is_prime(fib[k]):
                k += 1
            matrix[i][j] = fib[k]
            k += 1
    return matrix