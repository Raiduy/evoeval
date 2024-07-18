
def intersection(interval1, interval2):
    """Determine if the intersection length of two intervals is a prime number."""
    # Calculate the intersection
    start_max = max(interval1[0], interval2[0])
    end_min = min(interval1[1], interval2[1])
    
    # Check if there is an intersection
    if start_max > end_min:
        return "NO"
    
    # Calculate the length of the intersection
    intersection_length = end_min - start_max
    
    # Check if the length is a prime number
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
