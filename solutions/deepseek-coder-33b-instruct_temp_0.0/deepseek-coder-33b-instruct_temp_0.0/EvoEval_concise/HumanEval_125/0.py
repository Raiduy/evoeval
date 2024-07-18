
def split_words(txt):
    """
    This function accepts a string and returns a list of words. It splits the string on whitespace. If there's no whitespace, it splits on commas. If there are no commas, the function returns the count of lowercase letters at odd positions in the alphabet(ord('a')=0, ord('b')=1,...,ord('z')=25).
    eg:
    split_words("Hello world!") returns ["Hello", "world!"]
    split_words("Hello,world!") returns ["Hello", "world!"]
    split_words("abcdef") returns 3 
    """
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum((1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 != 0))