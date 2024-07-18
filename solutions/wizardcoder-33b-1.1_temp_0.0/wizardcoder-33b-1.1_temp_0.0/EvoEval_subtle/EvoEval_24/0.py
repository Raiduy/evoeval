
def smallest_divisor(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1 """
    for i in range(2, n + 1):
        if n % i == 0:
            return i