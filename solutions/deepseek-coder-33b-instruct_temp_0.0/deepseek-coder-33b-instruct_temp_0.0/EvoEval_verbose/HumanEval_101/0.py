
def words_string(s):
    """
    This function takes as input a string of words that may be separated by either commas or spaces. 

    The purpose of this function is to effectively process the input string, by separating it into its component words. 
    It achieves this by splitting the string wherever a comma or a space is encountered. The split words are then stored 
    in an array, which is returned as the output of the function. 

    An important aspect to note is that the input string can contain an arbitrary number of words, and the words can be 
    separated by either a comma, a space, or a combination of both.

    Args:
    s (str): A string of words separated by either commas or spaces.

    Returns:
    list: A list containing the words from the input string, split on the basis of commas and spaces.

    Examples:
    The function is expected to perform in the following way:

    words_string("Hi, my name is John") returns ["Hi", "my", "name", "is", "John"]
    In the above example, the input string contains five words separated by either a comma or a space.
    The function splits the string into five separate words and returns them as elements of a list.

    words_string("One, two, three, four, five, six") returns ["One", "two", "three", "four", "five", "six"]
    In this example, the input string contains six words, all separated by commas and spaces. 
    Again, the function splits the string into six separate words and returns them as elements of a list.
    """
    return s.replace(',', '').split()