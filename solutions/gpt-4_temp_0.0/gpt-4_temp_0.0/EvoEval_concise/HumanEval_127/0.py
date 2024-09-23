
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
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start > end:
        return 'NO'
    else:
        length = end - start + 1
        return 'YES' if is_prime(length) else 'NO'