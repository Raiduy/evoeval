from typing import List

def advanced_fizz_buzz(n: int, divisors: List[int], target: int) -> int:

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            (a, b) = (0, 1)
            for _ in range(2, n + 1):
                (a, b) = (b, a + b)
            return b
    count = 0
    for i in range(1, n + 1):
        if any((i % d == 0 for d in divisors)):
            fib = str(fibonacci(i))
            count += fib.count(str(target))
    return count