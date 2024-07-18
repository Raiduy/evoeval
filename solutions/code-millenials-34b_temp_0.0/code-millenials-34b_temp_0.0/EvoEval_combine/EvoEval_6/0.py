
def pile_median(n):
    if n % 2 == 0:
        median = (n + n + 1) / 2
        return float(median)
    else:
        median = n + 1
        return int(median)