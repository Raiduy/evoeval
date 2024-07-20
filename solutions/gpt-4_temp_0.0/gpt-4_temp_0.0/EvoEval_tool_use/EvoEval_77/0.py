def parse_string(s):
    '''
    This is a helper function. It takes a string s and returns the string 
    without any punctuation and all in lower case.
    '''
    import string 

    # remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))

    # convert to lower case
    s = s.lower()
    
    return s
def is_isogram(s):
    """
    Write a function that takes a string s and returns True if s is an isogram.
    An isogram is a word or phrase without a repeating letter (case in-sensitive and after removing punctuations).
    Note: you may assume the input is always valid.
    Examples:
    is_isogram("Dermatoglyphics") ==> True
    is_isogram("aba") ==> False
    is_isogram("moOse") ==> False
    is_isogram("isograms") ==> True
    """
    s = parse_string(s)
    return len(s) == len(set(s))