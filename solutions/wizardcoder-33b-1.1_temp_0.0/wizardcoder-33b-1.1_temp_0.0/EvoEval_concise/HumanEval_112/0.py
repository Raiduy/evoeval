
def reverse_delete(s, c):
    s = ''.join([char for char in s if char not in c])
    is_palindrome = s == s[::-1]
    return (s, is_palindrome)