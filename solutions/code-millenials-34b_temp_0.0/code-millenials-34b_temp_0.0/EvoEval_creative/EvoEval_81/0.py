def alien_language(word_list, alien_dictionary):
    if not word_list:
        return 'CORRECT'
    alien_order = {char: idx for (idx, char) in enumerate(alien_dictionary)}
    for i in range(len(word_list) - 1):
        word1 = word_list[i]
        word2 = word_list[i + 1]
        min_len = min(len(word1), len(word2))
        if word1[:min_len] > word2[:min_len]:
            return 'INCORRECT'
        if len(word1) > len(word2):
            return 'INCORRECT'
        for (char1, char2) in zip(word1, word2):
            if alien_order[char1] > alien_order[char2]:
                return 'INCORRECT'
    return 'CORRECT'