def spell_casting(strings):
    """
    You're a wizard and you have a list of spells represented as strings. Each of these spells consists 
    of several words. However, you can't just cast them in the order they are given. You have to sort 
    the words in each spell based on their length. If two words have the same length, keep them in the 
    original order.

    Write a function that accepts a list of strings (spells) and returns a list where each spell string 
    has its words sorted as per the rule outlined above.

    Example:
    >>> spell_casting(["hocus pocus", "wingardium leviosa", "expecto patronum"])
    ['hocus pocus', 'leviosa wingardium', 'expecto patronum']

    >>> spell_casting(["accio", "expelliarmus", "stupefy"])
    ['accio', 'expelliarmus', 'stupefy']

    Note: You can assume that all words in the spells are separated by a single space and there are no punctuation marks.
    """
    sorted_spells = []
    for spell in strings:
        words = spell.split()
        sorted_words = sorted(words, key=len)
        sorted_spells.append(' '.join(sorted_words))
    return sorted_spells