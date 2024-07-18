def starts_one_ends(n, x, y):
    """
    Given three positive integers n, x, y, return the count of the numbers of n-digit
    positive integers that start with digit x or end with digit y. The function should also handle
    inputs where n is up to 5. In addition, if there is no n-digit number that fits the criteria, or
    violates the constraint or x or y is not a digit, return -1.
    """
    if not 1 <= x <= 9 or not 0 <= y <= 9 or n < 1 or (n > 5):
        return -1
    if n == 1:
        return 1 if x == y else 2
    start_with_x = 10 ** (n - 1)
    end_with_y = 9 * 10 ** (n - 2)
    overlap = 10 ** (n - 2) if n > 2 else 1
    total_count = start_with_x + end_with_y - overlap
    return total_count