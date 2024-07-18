def magical_seven(n: int):
    """
    magical_seven returns the n-th number that is a multiple of 7 and its digits sum up to 7.
    
    >>> magical_seven(1)
    7
    >>> magical_seven(2)
    70
    >>> magical_seven(3)
    133
    >>> magical_seven(4)
    322
    >>> magical_seven(5)
    511
    """
    count = 0
    num = 0
    while count < n:
        num += 1
        if num % 7 == 0 and sum((int(digit) for digit in str(num))) == 7:
            count += 1
    return num