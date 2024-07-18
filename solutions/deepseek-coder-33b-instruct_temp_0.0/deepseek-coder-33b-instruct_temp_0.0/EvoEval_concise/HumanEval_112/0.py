
def reverse_delete(s, c):
    """
    Given two strings 's' and 'c', delete all characters in 's' equal to characters in 'c', 
    then determine if the resulting string is a palindrome (reads same backward as forward). 
    Return a tuple with the result string and a boolean indicating palindrome status.
    """
    s = ''.join([char for char in s if char not in c])
    is_palindrome = s == s[::-1]
    return (s, is_palindrome)