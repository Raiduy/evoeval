def magical_sequence(sequence, k):

    def count_points(num):
        points = 0
        while num > 1:
            num /= k
            points += 1
        return points
    sequence.sort(key=count_points, reverse=True)
    return sequence