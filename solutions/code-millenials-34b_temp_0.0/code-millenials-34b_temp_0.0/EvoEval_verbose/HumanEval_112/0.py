
def reverse_delete(s, c):
    for char in c:
        s = s.replace(char, '')
    is_palindrome = s == s[::-1]
    return (s, is_palindrome)