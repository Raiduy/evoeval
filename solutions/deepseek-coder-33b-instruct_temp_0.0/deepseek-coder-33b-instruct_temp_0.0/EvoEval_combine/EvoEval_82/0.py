
def odd_fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib = [0, 0, 1]
        for i in range(3, n + 1):
            fibfib.append(fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3])
            if fibfib[i] % 2 == 0:
                digits = [int(d) for d in str(fibfib[i]) if int(d) % 2 != 0]
                if len(digits) == 0:
                    fibfib[i] = 0
                else:
                    product = 1
                    for digit in digits:
                        product *= digit
                    fibfib[i] = product
        return fibfib[n]