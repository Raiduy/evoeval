
def solution(lst):
    """
    Calculates the sum of odd numbers at even-indexed positions in a given integer list.

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    sum = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum