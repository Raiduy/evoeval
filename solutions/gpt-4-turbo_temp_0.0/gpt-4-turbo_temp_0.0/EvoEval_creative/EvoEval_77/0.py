def magical_sequence(sequence, k):

    def calculate_points(number):
        points = 0
        while number % k == 0 and number > 1:
            number //= k
            points += 1
        return points
    points_list = [calculate_points(num) for num in sequence]
    points_list.sort(reverse=True)
    return points_list