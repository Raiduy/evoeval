def magical_sequence(sequence, k):
    """
    Imagine a magical sequence where each number is associated with a certain number of points. 
    The points for each number are equivalent to the number of times the number can be divided by k until it reaches 1. 
    Now, given a sequence of positive integers and a positive integer k, 
    return a list sorted in decreasing order of the total points each number in the sequence can achieve.

    Example 1:

        Input: sequence = [8, 5, 3], k = 2
        Output: [3, 0, 0]

    Example 2:

        Input: sequence = [25, 10, 5], k = 5
        Output: [2, 1, 1]

    Example 3:

        Input: sequence = [12, 8, 6, 4], k = 2
        Output: [3, 2, 2, 1]
    """
    points = []
    for num in sequence:
        point = 0
        while num >= k:
            if num % k == 0:
                num = num / k
                point += 1
            else:
                break
        points.append(point)
    points.sort(reverse=True)
    return points