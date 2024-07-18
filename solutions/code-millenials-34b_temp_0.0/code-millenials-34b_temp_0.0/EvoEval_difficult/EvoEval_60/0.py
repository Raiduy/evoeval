def sum_to_n_positive_odd(n: int):
    if not isinstance(n, int) or n < 1:
        return 'Input must be a positive integer.'
    modulo = 10 ** 9 + 7
    sum_odd = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum_odd = (sum_odd + i) % modulo
    return sum_odd