
def select_words(s, n):
    """Return a list of words from string s that contain exactly n consonants, in their original order. 
    If string s is empty, return an empty list. 
    It is assumed that the input string only contains letters and spaces. 
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    vowels = 'aeiou'
    words = s.split()
    result = []
    for word in words:
        count = sum((1 for char in word if char.lower() not in vowels))
        if count == n:
            result.append(word)
    return result