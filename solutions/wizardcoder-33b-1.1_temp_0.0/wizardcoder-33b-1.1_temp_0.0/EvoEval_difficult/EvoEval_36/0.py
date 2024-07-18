from typing import List

def advanced_fizz_buzz(n: int, divisors: List[int], target: int) -> int:
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    fib.pop()
    fib = [x for x in fib if any((x % d == 0 for d in divisors))]
    return sum((str(x).count(str(target)) for x in fib))