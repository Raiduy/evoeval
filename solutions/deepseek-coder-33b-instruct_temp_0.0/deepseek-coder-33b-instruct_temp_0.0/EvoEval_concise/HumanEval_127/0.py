
def intersection(interval1, interval2):
    """
    Given two closed intervals of integers, determine whether the length of their intersection is a prime number. 
    Closed intervals include both start and end, and start is always less or equal to end. 
    If the intersection's length is prime, return "YES". If not or if the intervals don't intersect, return "NO".
    
    Examples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """

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
        return 'NO'
    intersection_length = end - start + 1
    return 'YES' if is_prime(intersection_length) else 'NO'