
def odd_fibfib(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    (a, b, c) = (0, 0, 1)
    for _ in range(3, n + 1):
        next_element = a + b + c
        if next_element % 2 == 0:
            next_element = product_of_odd_digits(next_element)
        (a, b, c) = (b, c, next_element)
    return c