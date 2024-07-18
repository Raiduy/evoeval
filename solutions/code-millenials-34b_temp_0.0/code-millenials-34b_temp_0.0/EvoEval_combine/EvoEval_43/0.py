
def sorted_fib4_sequence(n: int):
    fib4 = [0, 0, 2, 0]
    for i in range(4, n):
        fib4.append(fib4[i - 1] + fib4[i - 2] + fib4[i - 3] + fib4[i - 4])
    if (fib4[0] + fib4[-1]) % 2 == 0:
        return sorted(fib4, reverse=True)
    else:
        return sorted(fib4)