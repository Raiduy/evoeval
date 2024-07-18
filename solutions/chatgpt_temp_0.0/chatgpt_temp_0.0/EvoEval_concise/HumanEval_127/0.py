
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
    (start1, end1) = interval1
    (start2, end2) = interval2
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    if intersection_start > intersection_end:
        return 'NO'
    intersection_length = intersection_end - intersection_start + 1
    if intersection_length <= 1:
        return 'NO'
    for i in range(2, int(intersection_length ** 0.5) + 1):
        if intersection_length % i == 0:
            return 'NO'
    return 'YES'