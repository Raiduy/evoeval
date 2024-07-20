
def even_odd_zero_sum(l, n):
    """
    even_odd_zero_sum takes a list of integers `l` and a positive integer `n` as inputs.
    
    It first calculates the number of even and odd integer palindromes that fall within the range(1, n), inclusive.
    
    It then checks if there are two distinct elements in the list `l` that sum to either of the two numbers obtained from the previous step.
    
    The function should return a tuple of two booleans. The first boolean indicates whether there are two distinct elements in the list `l` that sum to the number of even palindromes, and the second boolean indicates the same for odd palindromes.
 
    Example:
        Input: l = [1, 3, -2, -3, -1, 5, -2], n = 10
        Output: (True, False)
        Explanation:
        Integer palindromes within the range (1, 10) are 1, 2, 3, 4, 5, 6, 7, 8, 9. There are 4 even palindromes and 5 odd palindromes.
        In the list `l`, there are two distinct elements that sum to 4 (3, 1) but there are no two distinct elements that sum to 5.
        
    Note:
        1. 1 <= n <= 10^3
        2. List `l` can contain both positive and negative integers.
        3. Distinct elements mean that the same element cannot be used twice to make the sum.
    """

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    def has_two_elements_sum(lst, target):
        seen = set()
        for num in lst:
            if target - num in seen:
                return True
            seen.add(num)
        return False
    even_palindromes = sum((1 for i in range(1, n + 1) if is_palindrome(i) and i % 2 == 0))
    odd_palindromes = sum((1 for i in range(1, n + 1) if is_palindrome(i) and i % 2 != 0))
    return (has_two_elements_sum(l, even_palindromes), has_two_elements_sum(l, odd_palindromes))