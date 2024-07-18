def magical_sequence(sequence, k):

    def count_points(n):
        points = 0
        while n != 1:
            n = n // k
            points += 1
        return points
    sequence.sort(key=count_points, reverse=True)
    return sequence