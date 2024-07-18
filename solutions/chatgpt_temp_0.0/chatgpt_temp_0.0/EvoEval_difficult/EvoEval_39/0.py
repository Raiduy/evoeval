def prime_fib_matrix(n: int, m: int):

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            (a, b) = (0, 1)
            for _ in range(2, n + 1):
                (a, b) = (b, a + b)
            return b

    def find_prime_fib_with_k(k):
        count = 0
        num = 1
        while count < k:
            num += 1
            if is_prime(num) and fibonacci(num):
                count += 1
        return num
    matrix = [[find_prime_fib_with_k(i * j) for j in range(m)] for i in range(n)]
    return matrix