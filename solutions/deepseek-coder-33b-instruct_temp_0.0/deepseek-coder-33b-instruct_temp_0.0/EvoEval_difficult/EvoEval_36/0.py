from typing import List

def advanced_fizz_buzz(n: int, divisors: List[int], target: int) -> int:

    def fibonacci(n: int) -> List[int]:
        fib_sequence = [0, 1]
        while fib_sequence[-1] + fib_sequence[-2] < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    def count_target(num: int, target: int) -> int:
        return str(num).count(str(target))
    fib_sequence = fibonacci(n)
    count = 0
    for num in fib_sequence:
        if any((num % div == 0 for div in divisors)):
            count += count_target(num, target)
    return count