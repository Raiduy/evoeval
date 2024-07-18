def customFibFib(n: int, startSequence: list, p: int):
    if n == 0:
        return startSequence[0]
    elif n == 1:
        return startSequence[1]
    elif n == 2:
        return startSequence[2]
    else:
        fib = startSequence[:]
        for i in range(3, n + 1):
            fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3])
            if fib[i] > p:
                return 'Limit Exceeded'
        return fib[n]