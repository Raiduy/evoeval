def magical_sequence(sequence, k):
    points = []
    for num in sequence:
        count = 0
        while num % k == 0:
            count += 1
            num //= k
        points.append(count)
    points.sort(reverse=True)
    return points