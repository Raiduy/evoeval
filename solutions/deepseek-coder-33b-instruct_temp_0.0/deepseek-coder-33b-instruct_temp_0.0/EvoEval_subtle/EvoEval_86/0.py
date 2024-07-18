
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    descending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'iH'
    anti_shuffle('hello') returns 'ollhe'
    anti_shuffle('Hello World!!!') returns 'olleH roldW!!!'
    """
    words = s.split(' ')
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word, reverse=True))
        ordered_words.append(ordered_word)
    return ' '.join(ordered_words)