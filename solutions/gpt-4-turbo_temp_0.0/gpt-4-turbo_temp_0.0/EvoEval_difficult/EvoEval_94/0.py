def complexity_increased(lst, n):
    """
    Find all prime numbers in the list and return the sum of nth power of their digits.
    """
    if not any((num > 0 for num in lst)):
        return -1
    sum_of_powers = 0
    for num in lst:
        if is_prime(num):
            sum_of_powers += sum((int(digit) ** n for digit in str(num)))
    return sum_of_powers if sum_of_powers > 0 else -1