
def odd_fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib = [0, 0, 1]
        for i in range(3, n + 1):
            fibfib.append(fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3])
            if fibfib[i] % 2 == 0:
                fibfib[i] = product_of_odd_digits(fibfib[i])
        return fibfib[n]