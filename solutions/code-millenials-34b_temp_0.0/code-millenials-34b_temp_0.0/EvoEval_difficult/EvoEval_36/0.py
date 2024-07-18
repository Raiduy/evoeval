from typing import List

def advanced_fizz_buzz(n: int, divisors: List[int], target: int) -> int:
    fib_sequence = fibonacci(n)
    count = 0
    for num in fib_sequence:
        if any((num % divisor == 0 for divisor in divisors)):
            count += str(num).count(str(target))
    return count