
def even_odd_zero_sum(l, n):
    even_palindromes = 0
    odd_palindromes = 0
    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1

    def has_two_elements_with_sum(lst, target):
        seen = set()
        for num in lst:
            if target - num in seen:
                return True
            seen.add(num)
        return False
    even_sum_exists = has_two_elements_with_sum(l, even_palindromes)
    odd_sum_exists = has_two_elements_with_sum(l, odd_palindromes)
    return (even_sum_exists, odd_sum_exists)