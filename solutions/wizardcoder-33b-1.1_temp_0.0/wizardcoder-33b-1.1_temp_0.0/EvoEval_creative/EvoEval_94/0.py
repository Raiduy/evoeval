def spell_casting(spells):
    result = []
    for spell in spells:
        words = spell.split()
        words.sort(key=len)
        result.append(' '.join(words))
    return result