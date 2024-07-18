def magical_seven(n: int) -> int:
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

    def sum_of_digits(num: int) -> int:
        """Helper function to calculate the sum of digits of a number."""
        return sum((int(digit) for digit in str(num)))
    count = 0
    current_num = 0
    while True:
        if current_num % 7 == 0 and sum_of_digits(current_num) == 7:
            count += 1
            if count == n:
                return current_num
        current_num += 1