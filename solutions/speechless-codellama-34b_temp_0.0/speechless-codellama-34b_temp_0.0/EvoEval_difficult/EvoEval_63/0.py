def customFibFib(n: int, startSequence: list, p: int) -> int:
    if n == 0:
        return startSequence[0]
    elif n == 1:
        return startSequence[1]
    elif n == 2:
        return startSequence[2]
    else:
        (a, b, c) = startSequence
        for i in range(3, n + 1):
            (a, b, c) = (b, c, a + b + c)
            if c > p:
                return 'Limit Exceeded'
        return c