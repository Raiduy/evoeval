
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start with 1 or end with 2.
    """
    count = 0
    for i in range(10 ** (n - 1), 10 ** n):
        if str(i)[0] == '1' or str(i)[-1] == '2':
            count += 1
    return count