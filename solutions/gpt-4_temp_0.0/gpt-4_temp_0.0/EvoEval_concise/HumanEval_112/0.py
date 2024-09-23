
def reverse_delete(s, c):
    """Task
    Given two strings 's' and 'c', delete all characters in 's' equal to characters in 'c', 
    then determine if the resulting string is a palindrome (reads same backward as forward). 
    Return a tuple with the result string and a boolean indicating palindrome status.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    result = ''.join([i for i in s if i not in c])
    is_palindrome = result == result[::-1]
    return (result, is_palindrome)