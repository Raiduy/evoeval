
def rounded_avg(n, m):
    """Given two positive integers n and m, calculate the average of all integers from n to m (inclusive),
    rounded to the nearest integer, then converted to binary. If n > m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1
    avg = round((n + m) * (m - n + 1) / 2 / (m - n + 1))
    return bin(avg)