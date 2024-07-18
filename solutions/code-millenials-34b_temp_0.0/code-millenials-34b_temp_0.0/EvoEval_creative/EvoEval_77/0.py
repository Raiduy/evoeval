def magical_sequence(sequence, k):
    result = []
    for num in sequence:
        points = 0
        while num >= k:
            points += 1
            num = num // k
        result.append(points)
    return result