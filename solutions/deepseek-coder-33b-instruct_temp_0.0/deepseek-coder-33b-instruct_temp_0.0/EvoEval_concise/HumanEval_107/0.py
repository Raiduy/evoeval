
def even_odd_palindrome(n):
    """
    Returns a tuple with the count of even and odd integer palindromes from 1 to n (inclusive).

    Args:
    n: Integer (1 <= n <= 10^3)

    Returns:
    A tuple with first element as count of even palindromes and second element as count of odd palindromes.

    Example:

        Input: even_odd_palindrome(3)
        Output: (1, 2)
        Explanation: Palindromes are 1, 2, 3; 1 even and 2 odd.

        Input: even_odd_palindrome(12)
        Output: (4, 6)
        Explanation: Palindromes are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11; 4 even and 6 odd.
    """

    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if is_palindrome(i):
            if len(str(i)) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)