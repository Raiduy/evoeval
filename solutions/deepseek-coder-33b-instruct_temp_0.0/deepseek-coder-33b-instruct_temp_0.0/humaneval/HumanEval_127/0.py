
def intersection(interval1, interval2):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if start > end:
        return "NO"

    length = end - start + 1
    return "YES" if is_prime(length) else "NO"
