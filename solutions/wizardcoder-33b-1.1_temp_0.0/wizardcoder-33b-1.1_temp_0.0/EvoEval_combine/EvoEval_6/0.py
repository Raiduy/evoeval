
def pile_median(n):
    total_stones = sum(range(n, 2 * n))
    median = total_stones / 2.0
    return int(median) if n % 2 == 1 else median