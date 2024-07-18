def spell_casting(strings):
    result = []
    for spell in strings:
        words = spell.split()
        words.sort(key=len)
        result.append(' '.join(words))
    return result