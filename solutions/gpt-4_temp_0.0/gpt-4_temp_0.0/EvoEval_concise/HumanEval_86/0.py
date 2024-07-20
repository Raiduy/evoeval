
def anti_shuffle(s):
    """
    This function accepts a string and returns a modified version where each word (separated by spaces) is replaced
    by an alphabetically sorted version of itself. The original order of words and spaces remains unchanged.

    For example:
    anti_shuffle('Hi') -> 'Hi'
    anti_shuffle('hello') -> 'ehllo'
    anti_shuffle('Hello World!!!') -> 'Hello !!!Wdlor'
    """
    words = s.split(' ')
    sorted_words = [''.join(sorted(word)) for word in words]
    return ' '.join(sorted_words)