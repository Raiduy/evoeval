
def sum_to_n(n: int, m: int=1):
    """sum_to_n is a function that sums numbers from m to n.
    >>> sum_to_n(30, 10)
    420
    >>> sum_to_n(100, 50)
    3825
    >>> sum_to_n(5, 2)
    14
    >>> sum_to_n(10, 5)
    45
    >>> sum_to_n(1, 1)
    1
    """
    return sum(range(m, n + 1))