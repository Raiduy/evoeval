
def strange_word_sort(text):
    """
    Given a string text where words are separated by one or more spaces,
    create a new string where the words are sorted in a strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining words, then minimum and so on.
    The comparison of words is case-insensitive. 
    If there are more than 2 consecutive spaces between words, replace them with -.
    If there is one space, replace it with underscore.

    Examples:
    strange_word_sort("apple Banana APPLE BANANA") == 'apple_BANANA_APPLE_Banana'
    strange_word_sort("  cat  dog   bird  ") == '__bird__dog-cat__'
    strange_word_sort("House   car") == 'car-House'
    strange_word_sort("") == ""
    """
    words = text.split()
    words.sort(key=str.lower)
    result = []
    while words:
        result.append(words.pop(0))
        if words:
            result.append(words.pop())
    result = ' '.join(result)
    result = result.replace('  ', '-')
    result = result.replace(' ', '_')
    return result