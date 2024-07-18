
def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    # Check if the intervals don't intersect
    if end1 < start2 or end2 < start1:
        return "NO"

    # Calculate the length of the intersection
    intersection_length = min(end1, end2) - max(start1, start2) + 1

    # Check if the length is a prime number
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"

