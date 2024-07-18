
def fibfib_search(n: int, lst: list) -> int:
    """
    Implement a function that computes the n-th element of the FibFib sequence as defined by:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    
    The function should then evaluate a non-empty list of positive integers, and return the greatest 
    integer in the list that is greater than zero, and has a frequency equal to or greater than the value
    of the calculated n-th FibFib element. The frequency of an integer is the number of times it appears 
    in the list.

    If no such value exists, return -1.

    Examples:
        fibfib_search(5, [4, 1, 2, 2, 3, 1, 1, 1, 1]) == 1
        fibfib_search(3, [1, 2, 2, 3, 3, 3, 4, 4, 4]) == 4
        fibfib_search(6, [5, 5, 4, 4, 4, 1, 1, 1, 1, 1]) == -1
    """
    fibfib_n = fibfib(n)
    frequency_dict = {}
    for element in lst:
        if element > 0:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1
    result = -1
    for (key, value) in frequency_dict.items():
        if value >= fibfib_n and key > result:
            result = key
    return result