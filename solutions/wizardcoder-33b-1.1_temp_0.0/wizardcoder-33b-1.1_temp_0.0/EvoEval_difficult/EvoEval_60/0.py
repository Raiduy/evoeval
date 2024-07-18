def sum_to_n_positive_odd(n: int):
    if not isinstance(n, int) or n < 1:
        return 'Input must be a positive integer.'
    else:
        return sum((i for i in range(1, n + 1) if i % 2 != 0)) % 107