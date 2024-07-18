
def intersection(interval1, interval2):
    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])
    if intersection_start > intersection_end:
        return 'NO'
    intersection_length = intersection_end - intersection_start + 1
    if intersection_length > 1:
        for i in range(2, intersection_length):
            if intersection_length % i == 0:
                return 'NO'
        else:
            return 'YES'
    else:
        return 'NO'