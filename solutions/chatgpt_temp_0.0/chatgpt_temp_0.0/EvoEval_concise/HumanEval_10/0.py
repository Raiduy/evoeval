def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Creates the shortest possible palindrome starting with the given string.
    
    The algorithm identifies the longest suffix palindrome in the substring and reverses any preceding text to append at the end of the string.
    
    Examples: 
    make_palindrome(''): returns ''
    make_palindrome('cat'): returns 'catac'
    make_palindrome('cata'): returns 'catac'
    """
    if not string:
        return ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            return string + string[:i][::-1]
    return string + string[1:][::-1]