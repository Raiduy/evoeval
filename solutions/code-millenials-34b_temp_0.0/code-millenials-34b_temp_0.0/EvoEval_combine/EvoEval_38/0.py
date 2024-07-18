
def even_odd_zero_sum(l, n):

    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    even_palindromes = [i for i in range(1, n) if i % 2 == 0 and is_palindrome(i)]
    odd_palindromes = [i for i in range(1, n) if i % 2 != 0 and is_palindrome(i)]
    even_sum = len(even_palindromes)
    odd_sum = len(odd_palindromes)
    even_bool = any((even_sum in [sum(pair) for pair in zip(l[:-1], l[1:])] for _ in range(len(l) - 1)))
    odd_bool = any((odd_sum in [sum(pair) for pair in zip(l[:-1], l[1:])] for _ in range(len(l) - 1)))
    return (even_bool, odd_bool)