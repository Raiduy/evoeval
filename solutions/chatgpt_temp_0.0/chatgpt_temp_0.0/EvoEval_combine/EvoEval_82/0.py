
def odd_fibfib(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib = [0, 0, 1]
        for i in range(3, n + 1):
            fibfib.append(fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3])
            if fibfib[i] % 2 == 0:
                digits = [int(digit) for digit in str(fibfib[i]) if int(digit) % 2 != 0]
                if len(digits) > 0:
                    fibfib[i] = 1
                    for digit in digits:
                        fibfib[i] *= digit
                else:
                    fibfib[i] = 0
        return fibfib[n]