
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string by comma or space. The pattern ',\s*|\s+' matches a comma followed by any amount of whitespace
    # or at least one whitespace character.
    words = re.split(',\s*|\s+', s)
    return words
