
def fibfib(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_values = [0, 0, 1]
        for i in range(3, n + 1):
            fibfib_values.append(fibfib_values[i - 3] + fibfib_values[i - 2] - fibfib_values[i - 1])
        return fibfib_values[n]