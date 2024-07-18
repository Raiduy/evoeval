def unique_paths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    else:
        return unique_paths(m - 1, n) + unique_paths(m, n - 1)