
def words_string(s):
    """
    Given a string of words divided by commas or spaces, split the string into individual words. 
    Return an array containing these words.
    
    Example:
    words_string("Hi, my name is John") => ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") => ["One", "two", "three", "four", "five", "six"]
    """
    words = []
    split_words = s.split(',') if ',' in s else s.split(' ')
    for word in split_words:
        words.append(word.strip())
    return words