

def fib4(n: int) -> int:
    if n == 0 or n == 1 or n == 3:
        return 0
    elif n == 2:
        return 2
    else:
        fib4_sequence = [0, 0, 2, 0]
        for i in range(4, n + 1):
            fib4_sequence.append(sum(fib4_sequence[-4:]))
        return fib4_sequence[-1]