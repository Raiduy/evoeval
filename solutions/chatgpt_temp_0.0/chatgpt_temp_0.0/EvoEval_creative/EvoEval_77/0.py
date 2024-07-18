def magical_sequence(sequence, k):
    points = []
    for num in sequence:
        count = 0
        while num % k == 0:
            num //= k
            count += 1
        points.append(count)
    return sorted(points, reverse=True)