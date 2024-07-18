def prime_fib_matrix(n: int, m: int):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            k = i * j
            while not is_prime(k) or not is_fibonacci(k):
                k += 1
            row.append(k)
        matrix.append(row)
    return matrix