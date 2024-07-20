
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
    fibfib = [0, 0, 1]
    for i in range(3, n + 1):
        fibfib.append(fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3])
    nth_fibfib = fibfib[n]
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    max_num = -1
    for (num, freq) in freq_dict.items():
        if num > 0 and freq >= nth_fibfib and (num > max_num):
            max_num = num
    return max_num