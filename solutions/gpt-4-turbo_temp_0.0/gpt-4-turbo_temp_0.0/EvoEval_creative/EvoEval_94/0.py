def spell_casting(spells):
    """
    Sorts the words in each spell based on their length, maintaining the original order for words of the same length.
    """
    sorted_spells = []
    for spell in spells:
        words = spell.split()
        sorted_words = sorted(words, key=len)
        sorted_spell = ' '.join(sorted_words)
        sorted_spells.append(sorted_spell)
    return sorted_spells