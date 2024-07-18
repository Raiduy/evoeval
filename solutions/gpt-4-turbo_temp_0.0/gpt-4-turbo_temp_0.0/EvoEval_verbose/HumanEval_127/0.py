
def intersection(interval1, interval2):
    start_max = max(interval1[0], interval2[0])
    end_min = min(interval1[1], interval2[1])
    if start_max > end_min:
        return 'NO'
    intersection_length = end_min - start_max + 1
    if is_prime(intersection_length):
        return 'YES'
    else:
        return 'NO'