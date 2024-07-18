def spell_casting(strings):
    sorted_spells = []
    for spell in strings:
        words = spell.split()
        sorted_words = sorted(words, key=lambda x: (len(x), words.index(x)))
        sorted_spells.append(' '.join(sorted_words))
    return sorted_spells