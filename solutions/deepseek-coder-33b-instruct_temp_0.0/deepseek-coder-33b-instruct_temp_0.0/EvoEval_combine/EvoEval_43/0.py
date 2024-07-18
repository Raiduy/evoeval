
def sorted_fib4_sequence(n: int):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 0]
    elif n == 3:
        return [0, 0, 2]
    else:
        fib4 = [0, 0, 2, 0]
        for i in range(4, n):
            fib4.append(fib4[i - 1] + fib4[i - 2] + fib4[i - 3] + fib4[i - 4])
        if (fib4[0] + fib4[-1]) % 2 == 0:
            fib4.sort(reverse=True)
        else:
            fib4.sort()
        return fib4