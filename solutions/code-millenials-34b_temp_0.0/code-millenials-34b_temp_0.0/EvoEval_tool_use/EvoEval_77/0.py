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
    s = parse_string(s)
    return len(s) == len(set(s))