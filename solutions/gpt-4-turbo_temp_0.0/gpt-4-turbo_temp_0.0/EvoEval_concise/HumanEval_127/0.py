
def intersection(interval1, interval2):
    """
    Given two closed intervals of integers, determine whether the length of their intersection is a prime number. 
    Closed intervals include both start and end, and start is always less or equal to end. 
    If the intersection's length is prime, return "YES". If not or if the intervals don't intersect, return "NO".
    """
    start_max = max(interval1[0], interval2[0])
    end_min = min(interval1[1], interval2[1])
    intersection_length = end_min - start_max + 1
    if intersection_length > 0 and is_prime(intersection_length):
        return 'YES'
    else:
        return 'NO'