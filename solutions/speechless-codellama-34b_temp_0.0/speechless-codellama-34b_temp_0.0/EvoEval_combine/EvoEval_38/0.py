
def even_odd_zero_sum(l, n):
    even_palindromes = 0
    odd_palindromes = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1
    even_sum = False
    odd_sum = False
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == even_palindromes:
                even_sum = True
            if l[i] + l[j] == odd_palindromes:
                odd_sum = True
    return (even_sum, odd_sum)