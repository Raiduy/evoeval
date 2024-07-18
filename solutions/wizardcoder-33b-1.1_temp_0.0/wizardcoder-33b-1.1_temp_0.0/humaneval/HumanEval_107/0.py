
def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0

    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:  # check if the number is a palindrome
            if i % 2 == 0:  # check if the number is even
                even_count += 1
            else:  # the number is odd
                odd_count += 1

    return (even_count, odd_count)
