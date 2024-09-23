
def add(lst):
    """
    This function, named 'add', is designed to take in one input argument. The input argument is a non-empty list of integers, 'lst'. The function's task is to add up specific elements within this list. More specifically, it only adds elements that are even numbers and are located at odd indices within the list. 

    To put it simply, the function scans the list from the beginning. It skips the first element, processes the second, skips the third, and so on, checking if each processed element is an even number. If it is, the function adds it to a running total. If it's not, the function simply moves on to the next index. At the end of the process, the function returns this total.

    Here is an illustrative example of the function's execution:

    If we have a list [4, 2, 6, 7] as input:
    - The function will start at the second element, which is 2 (an even number at an odd index). It adds 2 to the total.
    - The function will skip the third element, which is 6.
    - The function will skip 7 since it is odd.

    Examples:
        add([4, 2, 6, 7]) ==> 2
    """
    total = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total