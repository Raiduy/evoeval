def cipher_mapping(s, cipher):
    """Given a string 's' and a mapping dictionary 'cipher', your task is to implement 
    a function that returns a new string where each character in 's' has been replaced 
    by its corresponding value in 'cipher'. 
    If a character in 's' does not exist in 'cipher', leave it as it is in the new string.
    If 's' is an empty string, the function should return an empty string.
    
    Examples:
    cipher_mapping("hello world", {'h':'y', 'e':'u', 'l':'q', 'o':'p', 'w':'j', 'r':'f', 'd':'m'}) 
    ==> 'yuqqp jpfqm'
    
    cipher_mapping("apple pie", {'a':'z', 'p':'r', 'l':'m', 'e':'s', 'i':'u'}) 
    ==> 'zrrms rus'
    
    cipher_mapping("simple test", {}) 
    ==> 'simple test'
    
    cipher_mapping("good day", {'g':'b', 'o':'a', 'd':'t', 'a':'g', 'y':'h'}) 
    ==> 'baat tgh'
    """
    return ''.join([cipher[c] if c in cipher else c for c in s])