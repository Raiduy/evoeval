
def even_odd_zero_sum(l, n):

    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    even_palindromes = sum((is_palindrome(i) and i % 2 == 0 for i in range(1, n + 1)))
    odd_palindromes = sum((is_palindrome(i) and i % 2 != 0 for i in range(1, n + 1)))
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == even_palindromes:
                return (True, False)
            if l[i] + l[j] == odd_palindromes:
                return (False, True)
    return (False, False)