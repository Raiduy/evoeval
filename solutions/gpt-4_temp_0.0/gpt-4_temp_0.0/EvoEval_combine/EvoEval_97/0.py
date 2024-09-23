
def fib_max_triples(n):
    fib = [0, 0, 1]
    for i in range(3, n + 1):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3] + i * i - i + 1)
    count = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if (fib[i] + fib[j] + fib[k]) % 3 == 0:
                    count += 1
    return count