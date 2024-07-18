
def even_odd_zero_sum(l, n):

    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    even_palindromes = [i for i in range(1, n + 1) if is_palindrome(i) and i % 2 == 0]
    odd_palindromes = [i for i in range(1, n + 1) if is_palindrome(i) and i % 2 != 0]
    even_sum = len(even_palindromes)
    odd_sum = len(odd_palindromes)
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == even_sum:
                return (True, False)
            if l[i] + l[j] == odd_sum:
                return (False, True)
    return (False, False)